# API Notes

## Endpoints

- Process request: `POST http://47.111.23.9/expense/process`
- Download HOA-001: `GET http://47.111.23.9/expense/download/{session_id}/hoa001`
- Download HOA-002: `GET http://47.111.23.9/expense/download/{session_id}/hoa002`
- Download all outputs: `GET http://47.111.23.9/expense/download/{session_id}/all`

## Upload Contract

- Use `multipart/form-data`.
- Upload travel approval PDFs as `travel_0`, `travel_1`, and so on.
- Upload invoice, itinerary, or receipt files as `invoice_0`, `invoice_1`, and so on.
- Approval files are identified from PDF filenames or their immediate parent folder names containing `商旅` or `出差`.
- Common invoice inputs can include PDF plus image files such as `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.tif`, and `.webp`.
- Treat every other supported file as an invoice or itinerary input.

## Expected Response

- Expect JSON containing:
  - a parsed-result preview
  - `session_id`
- Treat the request as failed if `session_id` is missing.

## Output Goal

- Download and surface:
  - `HOA-001出差费用报销汇总表.xls`
  - `HOA-002交通费明细单.xlsx`
- Save the full JSON response as `preview.json` for later checking.
- Download `all` only when the user explicitly requests the bundled archive.
