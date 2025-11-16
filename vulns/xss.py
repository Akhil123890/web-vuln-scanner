import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"'><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
]


def _send_get(url):
    return requests.get(url, timeout=5, verify=False)


def _send_post(url, data):
    return requests.post(url, data=data, timeout=5, verify=False)


def check_xss(url, params, method="GET"):
    findings = []

    for param in params:
        for payload in XSS_PAYLOADS:
            try:
                if method.upper() == "GET":
                    parsed = urlparse(url)
                    qs = parse_qs(parsed.query)
                    if param not in qs:
                        continue
                    qs[param] = [payload]
                    new_query = urlencode(qs, doseq=True)
                    new_url = urlunparse(parsed._replace(query=new_query))
                    resp = _send_get(new_url)
                    attack_url = new_url
                else:
                    data = {p: "test" for p in params}
                    data[param] = payload
                    resp = _send_post(url, data)
                    attack_url = url + " [POST]"
                body = resp.text
                if payload in body:
                    findings.append({
                        "type": "Cross-Site Scripting (XSS)",
                        "url": url,
                        "attack_url": attack_url,
                        "param": param,
                        "payload": payload,
                        "evidence": "Payload reflected in response.",
                        "severity": "High"
                    })
                    break
            except Exception:
                continue

    return findings
