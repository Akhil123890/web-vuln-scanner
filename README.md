# Web Application Vulnerability Scanner (Mini Burp Suite)

This is a simple educational **web application vulnerability scanner** written in Python.

It can:
- Crawl a target website (same-domain links)
- Identify URLs and forms with parameters
- Test for:
  - SQL Injection
  - Cross-Site Scripting (XSS)
  - Open Redirect
- Generate an HTML report

> **Important:** This tool is for learning and testing on **your own applications** or systems where you have **explicit permission**. Do not use it on unauthorized targets.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scanner.py --url https://example.com --depth 1 --report report.html
```

- `--url`   : Target website to scan
- `--depth` : Crawl depth (default: 1)
- `--report`: Output HTML report file name

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install using:

```bash
pip install requests beautifulsoup4
```

Or:

```bash
pip install -r requirements.txt
```

## Disclaimer

This project is for **educational purposes only**.
Use it responsibly and legally.
