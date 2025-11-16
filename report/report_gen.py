from datetime import datetime
import html


def generate_report(base_url, findings, filename):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'><title>Web Vulnerability Scan Report</title>")
        f.write("<style>body{font-family:Arial, sans-serif;margin:20px;} table{border-collapse:collapse;width:100%;} th,td{border:1px solid #ccc;padding:8px;text-align:left;} th{background:#eee;} .high{color:red;font-weight:bold;} .medium{color:orange;font-weight:bold;} .low{color:green;font-weight:bold;}</style>")
        f.write("</head><body>")
        f.write("<h1>Web Vulnerability Scan Report</h1>")
        f.write(f"<p><b>Target:</b> {html.escape(base_url)}</p>")
        f.write(f"<p><b>Generated at:</b> {now}</p>")
        f.write(f"<p><b>Total Findings:</b> {len(findings)}</p><hr>")

        if not findings:
            f.write("<p>No vulnerabilities detected with current payload set.</p>")
        else:
            f.write("<table>")
            f.write("<tr><th>#</th><th>Type</th><th>Severity</th><th>URL</th><th>Attack URL</th><th>Parameter</th><th>Payload</th><th>Evidence</th></tr>")
            for i, issue in enumerate(findings, 1):
                severity_class = issue.get("severity", "").lower()
                f.write("<tr>")
                f.write(f"<td>{i}</td>")
                f.write(f"<td>{html.escape(issue.get('type', '-'))}</td>")
                f.write(f"<td class='{severity_class}'>{html.escape(issue.get('severity', '-'))}</td>")
                f.write(f"<td>{html.escape(issue.get('url', '-'))}</td>")
                f.write(f"<td>{html.escape(issue.get('attack_url', '-'))}</td>")
                f.write(f"<td>{html.escape(issue.get('param', '-'))}</td>")
                f.write(f"<td>{html.escape(issue.get('payload', '-'))}</td>")
                f.write(f"<td>{html.escape(issue.get('evidence', '-'))}</td>")
                f.write("</tr>")
            f.write("</table>")

        f.write("<hr><p><i>Note: This is a basic academic scanner. Results may include false positives or miss complex vulnerabilities. Always validate manually.</i></p>")
        f.write("</body></html>")
