# 🔥 Web Application Vulnerability Scanner (Mini Burp Suite)


A lightweight, Python-based web application vulnerability scanner built for cybersecurity learning.

This tool automatically crawls a target website, identifies parameters, injects attack payloads, and detects common vulnerabilities including:

SQL Injection

Cross-Site Scripting (XSS)

Open Redirect

It also generates a professional, clean HTML security report.

# 🚀 Features

🔍 Automatic Web Crawler (extracts links, forms, parameters)

🧪 SQL Injection Detection

🧪 XSS (Cross-Site Scripting) Detection

🔁 Open Redirect Detection

📄 HTML Report Generation

🛠 Modular Architecture (easy to extend with new vulns)

🔧 Beginner-friendly Python code

# 🖥️ Tech Stack

Python 3.x

requests

beautifulsoup4

urllib.parse

HTML reporting module

> **Important:** This tool is for learning and testing on **your own applications** or systems where you have **explicit permission**. Do not use it on unauthorized targets.

# 📁 Project Structure

```bash
web-vuln-scanner/
│── scanner.py            # Main entry point
│── crawler.py            # Crawler module
│── requirements.txt
│── README.md
│
├── vulns/                # Vulnerability modules
│   ├── sqli.py
│   ├── xss.py
│   └── redirect.py
│
└── report/
    └── report_gen.py     # HTML report generator
```
## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/web-vuln-scanner.git
cd web-vuln-scanner
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the scanner with:

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

# 🛡️ Vulnerabilities Detected
1️⃣ SQL Injection (SQLi)

Error-based detection

Payload injection

Response analysis

2️⃣ Cross-Site Scripting (XSS)

Reflected XSS

Script injection payloads

HTML reflection checks

3️⃣ Open Redirect

Parameter testing

Redirection to external domain

# 📄 Sample Report Output

Target URL

Timestamp

Vulnerability list

Severity (High / Medium / Low)

Attack URLs

Payloads used

Evidence

# 🧭 Roadmap / Future Enhancements

Add CSRF detection

Add Directory Traversal detection

Add Command Injection detection

Add Login form authentication support

Add GUI dashboard (Flask / Tkinter)

Export reports as PDF / JSON

# 📚 Educational Disclaimer

This tool is for educational and authorized testing only.
Do NOT scan websites without permission.

Unauthorized scanning = illegal ✖️
Use responsibly ✔️
```

# Disclaimer

This project is for **educational purposes only**.
Use it responsibly and legally.
```

Unauthorized scanning = illegal ✖️

Use responsibly ✔️
