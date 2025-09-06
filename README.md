# AI-scripts
AI-powered Python scripts for faster development

## Prerequisites
- [uv](https://docs.astral.sh/uv/) - Python package manager
- Python 3.12+

## Scripts

### scraper
Extracts clean markdown content from web pages and copies it to clipboard. Removes navigation, ads, and other non-content elements.

**Usage:**
```bash
# Unix/Linux/macOS
chmod +x scraper
scraper <url>

# Windows (.ps1 wrapper)
scraper <url>

# Direct usage
uv run --script scraper <url>
```

**Example:**
```bash
scraper https://docs.crawl4ai.com/core/content-selection/
```


## How it works
- Scripts use uv's inline dependency management
- Dependencies are automatically installed when scripts run
- No virtual environment setup required