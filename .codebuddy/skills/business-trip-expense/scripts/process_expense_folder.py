#!/usr/bin/env python3
"""
Process a folder of business-trip reimbursement files through a remote API.
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import sys
import uuid
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple
from urllib import error, request


PROCESS_URL = "http://47.111.23.9/expense/process"
DOWNLOAD_BASE_URL = "http://47.111.23.9/expense/download"
TRAVEL_KEYWORDS = (
    "\u5546\u65c5",
    "\u51fa\u5dee",
)
COMPATIBILITY_KEYWORDS = (
    "\u935f\u55d8\u68be",
    "\u9351\u54c4\u6a0a",
)
KEYWORDS = TRAVEL_KEYWORDS + COMPATIBILITY_KEYWORDS
OUTPUT_NAMES = {
    "hoa001": "HOA-001\u51fa\u5dee\u8d39\u7528\u62a5\u9500\u6c47\u603b\u8868.xls",
    "hoa002": "HOA-002\u4ea4\u901a\u8d39\u660e\u7ec6\u5355.xlsx",
    "all": "expense-files.zip",
}
SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tiff",
    ".tif",
    ".webp",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upload approval PDFs and invoice PDF/image files to the reimbursement API.",
    )
    parser.add_argument(
        "folder",
        help="Folder containing approval PDFs plus invoice PDF/image files",
    )
    parser.add_argument(
        "--output-dir",
        help="Directory for downloaded outputs. Defaults to <folder>/expense-output-<session_id> after upload.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="HTTP timeout in seconds. Default: 120",
    )
    parser.add_argument(
        "--include-zip",
        action="store_true",
        help="Also download the server-provided zip package in addition to individual HOA files.",
    )
    return parser.parse_args()


def collect_supported_files(folder: Path) -> List[Path]:
    return sorted(
        path
        for path in folder.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def configure_stdio() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def is_travel_file(path: Path, root: Path) -> bool:
    if path.suffix.lower() != ".pdf":
        return False

    parts = [path.name]
    try:
        relative = path.relative_to(root)
        if len(relative.parts) > 1:
            parts.append(relative.parts[-2])
    except ValueError:
        parts.append(path.parent.name)
    return any(keyword in part for part in parts for keyword in KEYWORDS)


def classify_files(paths: Sequence[Path], root: Path) -> Tuple[List[Path], List[Path]]:
    travel = []
    invoices = []
    for path in paths:
        if is_travel_file(path, root):
            travel.append(path)
        else:
            invoices.append(path)
    return travel, invoices


def encode_multipart(files: Sequence[Tuple[str, Path]]) -> Tuple[bytes, str]:
    boundary = f"----CodexExpense{uuid.uuid4().hex}"
    chunks: List[bytes] = []
    for field_name, file_path in files:
        filename = file_path.name
        content_type = mimetypes.guess_type(filename)[0] or "application/pdf"
        file_bytes = file_path.read_bytes()
        chunks.extend(
            [
                f"--{boundary}\r\n".encode("utf-8"),
                (
                    f'Content-Disposition: form-data; name="{field_name}"; '
                    f'filename="{filename}"\r\n'
                ).encode("utf-8"),
                f"Content-Type: {content_type}\r\n\r\n".encode("utf-8"),
                file_bytes,
                b"\r\n",
            ]
        )
    chunks.append(f"--{boundary}--\r\n".encode("utf-8"))
    return b"".join(chunks), boundary


def post_files(files: Sequence[Tuple[str, Path]], timeout: int) -> dict:
    body, boundary = encode_multipart(files)
    req = request.Request(
        PROCESS_URL,
        data=body,
        method="POST",
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    with request.urlopen(req, timeout=timeout) as response:
        payload = response.read().decode("utf-8")
    return json.loads(payload)


def summarize_preview(payload: dict) -> str:
    preview = {key: value for key, value in payload.items() if key != "session_id"}
    return json.dumps(preview, ensure_ascii=False, indent=2)


def download_file(session_id: str, kind: str, output_path: Path, timeout: int) -> None:
    url = f"{DOWNLOAD_BASE_URL}/{session_id}/{kind}"
    with request.urlopen(url, timeout=timeout) as response:
        output_path.write_bytes(response.read())


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def build_upload_fields(travel: Sequence[Path], invoices: Sequence[Path]) -> List[Tuple[str, Path]]:
    fields: List[Tuple[str, Path]] = []
    fields.extend((f"travel_{idx}", path) for idx, path in enumerate(travel))
    fields.extend((f"invoice_{idx}", path) for idx, path in enumerate(invoices))
    return fields


def print_file_group(title: str, paths: Iterable[Path]) -> None:
    print(title)
    for path in paths:
        print(f"  - {path}")


def build_downloads(output_dir: Path, include_zip: bool) -> dict[str, Path]:
    downloads = {
        "hoa001": output_dir / OUTPUT_NAMES["hoa001"],
        "hoa002": output_dir / OUTPUT_NAMES["hoa002"],
    }
    if include_zip:
        downloads["all"] = output_dir / OUTPUT_NAMES["all"]
    return downloads


def main() -> int:
    configure_stdio()
    args = parse_args()
    folder = Path(args.folder).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        print(f"Folder not found or not a directory: {folder}", file=sys.stderr)
        return 1

    files = collect_supported_files(folder)
    if not files:
        print(
            f"No supported files found under: {folder}. Expected PDF or common image files.",
            file=sys.stderr,
        )
        return 1

    travel, invoices = classify_files(files, folder)
    if not travel:
        print(
            "No travel approval PDF found. Expected the filename or immediate parent folder to contain business-trip keywords.",
            file=sys.stderr,
        )
        return 1

    print_file_group("Travel approval PDFs:", travel)
    print_file_group("Invoice/itinerary files:", invoices)

    try:
        payload = post_files(build_upload_fields(travel, invoices), args.timeout)
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"API request failed with HTTP {exc.code}: {body}", file=sys.stderr)
        return 1
    except error.URLError as exc:
        print(f"API request failed: {exc}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"API returned non-JSON content: {exc}", file=sys.stderr)
        return 1

    session_id = payload.get("session_id")
    if not session_id:
        print("API response did not include session_id.", file=sys.stderr)
        print(json.dumps(payload, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1

    output_dir = (
        Path(args.output_dir).expanduser().resolve()
        if args.output_dir
        else folder / f"expense-output-{session_id}"
    )
    ensure_dir(output_dir)

    preview_path = output_dir / "preview.json"
    preview_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    downloads = build_downloads(output_dir, args.include_zip)
    for kind, output_path in downloads.items():
        try:
            download_file(session_id, kind, output_path, args.timeout)
        except error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            print(f"Download failed for {kind} with HTTP {exc.code}: {body}", file=sys.stderr)
            return 1
        except error.URLError as exc:
            print(f"Download failed for {kind}: {exc}", file=sys.stderr)
            return 1

    print(f"session_id: {session_id}")
    print("Preview:")
    print(summarize_preview(payload))
    print(f"preview.json: {preview_path}")
    print(f"hoa001: {downloads['hoa001']}")
    print(f"hoa002: {downloads['hoa002']}")
    if "all" in downloads:
        print(f"all: {downloads['all']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
