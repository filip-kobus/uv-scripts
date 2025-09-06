# !powershell
#
# Description: PowerShell wrapper to run the Python scraper script using uv

$PythonScriptPath = Join-Path $PSScriptRoot "scraper"

uv run --script $PythonScriptPath -- $args