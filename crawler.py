import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs


def crawl(start_url, max_depth=1, timeout=5):
    """
    Very simple crawler that:
    - Stays within the same domain
    - Collects URLs with query parameters
    - Collects forms and their input fields
    """
    visited = set()
    to_visit = [(start_url, 0)]
    targets = []

    domain = urlparse(start_url).netloc

    headers = {
        "User-Agent": "MiniWebScanner/1.0"
    }

    while to_visit:
        url, depth = to_visit.pop(0)

        if url in visited or depth > max_depth:
            continue
        visited.add(url)

        try:
            resp = requests.get(url, headers=headers, timeout=timeout, verify=False)
        except Exception:
            continue

        soup = BeautifulSoup(resp.text, "html.parser")

        # Collect query params from URL
        parsed = urlparse(url)
        params = list(parse_qs(parsed.query).keys())
        if params:
            targets.append({"url": url, "params": params, "method": "GET"})

        # Collect forms
        for form in soup.find_all("form"):
            form_method = form.get("method", "get").upper()
            form_action = form.get("action") or url
            form_url = urljoin(url, form_action)
            inputs = [i.get("name") for i in form.find_all(["input", "textarea", "select"]) if i.get("name")]
            if inputs:
                targets.append({"url": form_url, "params": inputs, "method": form_method})

        # Follow links
        for link in soup.find_all("a", href=True):
            link_url = urljoin(url, link["href"])
            parsed_link = urlparse(link_url)
            if parsed_link.netloc == domain and link_url not in visited:
                to_visit.append((link_url, depth + 1))

    return targets
