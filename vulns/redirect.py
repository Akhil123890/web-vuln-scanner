import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

REDIRECT_PARAMS = ["url", "redirect", "next", "dest", "destination"]
MALICIOUS_TARGET = "https://attacker.example.com/"


def _send_get(url, allow_redirects=True):
    return requests.get(url, timeout=5, verify=False, allow_redirects=allow_redirects)


def _send_post(url, data, allow_redirects=True):
    return requests.post(url, data=data, timeout=5, verify=False, allow_redirects=allow_redirects)


def check_open_redirect(url, params, method="GET"):
    findings = []

    for param in params:
        if param.lower() not in REDIRECT_PARAMS:
            continue
        try:
            if method.upper() == "GET":
                parsed = urlparse(url)
                qs = parse_qs(parsed.query)
                if param not in qs:
                    continue
                qs[param] = [MALICIOUS_TARGET]
                new_query = urlencode(qs, doseq=True)
                new_url = urlunparse(parsed._replace(query=new_query))
                resp = _send_get(new_url)
                attack_url = new_url
            else:
                data = {p: "test" for p in params}
                data[param] = MALICIOUS_TARGET
                resp = _send_post(url, data)
                attack_url = url + " [POST]"

            # Check final URL after redirects
            final_url = resp.url
            if MALICIOUS_TARGET.rstrip("/") in final_url.rstrip("/"):
                findings.append({
                    "type": "Open Redirect",
                    "url": url,
                    "attack_url": attack_url,
                    "param": param,
                    "payload": MALICIOUS_TARGET,
                    "evidence": f"Redirected to attacker-controlled URL: {final_url}",
                    "severity": "Medium"
                })
        except Exception:
            continue

    return findings
