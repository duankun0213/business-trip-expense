# API Notes

## Endpoints

- Process request: `POST http://47.111.23.9/expense/process`
- Download HOA-001: `GET http://47.111.23.9/expense/download/{session_id}/hoa001`
- Download HOA-002: `GET http://47.111.23.9/expense/download/{session_id}/hoa002`
- Download all outputs: `GET http://47.111.23.9/expense/download/{session_id}/all`

## Upload Contract

- Use `multipart/form-data`.
- Upload travel approval PDFs as `travel_0`, `travel_1`, and so on.
- Upload invoice or itinerary PDFs as `invoice_0`, `invoice_1`, and so on.
- Classify a PDF as a travel approval file when its filename or any parent folder name contains `商旅` or `出差`.
- Treat every other PDF as an invoice or itinerary file.

## Expected Response

- Expect JSON containing:
  - a parsed-result preview
  - `session_id`
- Treat the request as failed if `session_id` is missing.

## Output Goal

- Download and surface:
  - `HOA-001出差费用报销汇总表.xls`
  - `HOA-002交通费明细单.xlsx`
- Download `all` only when the user explicitly requests the bundled archive.
