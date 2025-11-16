import argparse
from crawler import crawl
from vulns.sqli import check_sqli
from vulns.xss import check_xss
from vulns.redirect import check_open_redirect
from report.report_gen import generate_report


def main():
    parser = argparse.ArgumentParser(description="Mini Web Application Vulnerability Scanner")
    parser.add_argument("--url", required=True, help="Target URL to scan, e.g., https://example.com")
    parser.add_argument("--depth", type=int, default=1, help="Crawl depth (default: 1)")
    parser.add_argument("--report", default="scan_report.html", help="Output report file name")
    args = parser.parse_args()

    print(f"[+] Starting crawl on {args.url} (depth={args.depth})")
    targets = crawl(args.url, max_depth=args.depth)
    print(f"[+] Discovered {len(targets)} potential targets (URLs/forms with parameters)")

    findings = []

    for t in targets:
        url, params, method = t["url"], t["params"], t["method"]
        print(f"[+] Scanning: {url} ({method}) params={params}")

        findings += check_sqli(url, params, method)
        findings += check_xss(url, params, method)
        findings += check_open_redirect(url, params, method)

    generate_report(args.url, findings, args.report)
    print(f"[+] Scan completed. Report saved to {args.report}")


if __name__ == "__main__":
    main()
