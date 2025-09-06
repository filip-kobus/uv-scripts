# 🚀 uv-scripts

A collection of Python scripts designed to work seamlessly with [uv](https://docs.astral.sh/uv/) for enhanced LLM and GenAI development workflows.

> **Note**: These scripts leverage uv's inline dependency management, making them easy to run without complex environment setup.

---

## � Table of Contents
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [How uv Scripts Work](#-how-uv-scripts-work)
- [Available Scripts](#️-available-scripts)
- [Contributing](#-contributing)

---

## 📦 Prerequisites

- **[uv](https://docs.astral.sh/uv/)** - Modern Python package manager  
   [Install uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)

---

## � Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/filip-kobus/AI-scripts.git
   cd AI-scripts
   ```

2. **Run any script directly**
   ```bash
   # Example: Extract content from a webpage
   uv run --script scraper https://example.com
   ```

---

## ⚡ How uv Scripts Work

[uv scripts](https://docs.astral.sh/uv/guides/scripts/) provide several advantages:

- **🔧 Inline dependency management** - Dependencies are declared within the script
- **📦 Automatic installation** - Dependencies are auto-installed when scripts run
- **🎯 No virtual environment needed** - uv handles isolation automatically
- **⚡ Fast execution** - uv's caching makes subsequent runs lightning fast

---

## 🛠️ Available Scripts

### 📝 scraper

**Purpose**: Extracts clean markdown content from web pages and copies it to your clipboard. Intelligently removes navigation, ads, and other non-content elements.

**Features**:
- 🧹 Clean content extraction
- 📋 Automatic clipboard copying
- 🚫 Removes ads and navigation
- 📱 Works on most websites

**Usage**:

```bash
# Make executable (Unix/Linux/macOS)
chmod +x scraper
scraper <url>

# Windows PowerShell wrapper
scraper <url>

# Direct uv execution (all platforms)
uv run --script scraper <url>
```

**Examples**:

```bash
# Extract documentation
scraper https://docs.crawl4ai.com/core/content-selection/

# Extract blog post
scraper https://medium.com/@author/article-title

# Extract technical article
scraper https://stackoverflow.com/questions/12345/question-title
```