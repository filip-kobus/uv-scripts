$PythonScriptPath = Join-Path $PSScriptRoot "scraper"

uv run --script $PythonScriptPath -- $args