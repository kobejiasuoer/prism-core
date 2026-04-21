# Demo Pipeline Architecture

The public demo pipeline is:

`stocks.json -> demo_loader -> demo_scan -> scorers -> demo_reviewer -> markdown_report`

Each step is intentionally simple so contributors can understand the workflow and extend it safely.
