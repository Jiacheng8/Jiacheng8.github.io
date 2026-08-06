import json
import os
import re
from datetime import datetime, timezone
from html import unescape
from urllib.parse import parse_qs, quote, urlparse
from urllib.request import Request, urlopen

scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
profile_url = (
    "https://scholar.google.com/citations"
    f"?user={quote(scholar_id)}&hl=en&pagesize=100"
)
request = Request(
    profile_url,
    headers={
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
        )
    },
)

html_fixture = os.environ.get("GOOGLE_SCHOLAR_HTML")
if html_fixture:
    with open(html_fixture, encoding="utf-8") as fixture:
        page = fixture.read()
else:
    with urlopen(request, timeout=30) as response:
        page = response.read().decode("utf-8")

name_match = re.search(r'<div id="gsc_prf_in"[^>]*>(.*?)</div>', page, re.DOTALL)
citation_match = re.search(r'class="gsc_rsb_std">([\d,]+)<', page)
if name_match is None or citation_match is None:
    raise RuntimeError("Google Scholar returned an unexpected page")

publications = {}
for row in re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, re.DOTALL):
    title_match = re.search(
        r'<a(?=[^>]*class="gsc_a_at")[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
        row,
        re.DOTALL,
    )
    if title_match is None:
        continue

    href, title = title_match.groups()
    query = parse_qs(urlparse(unescape(href)).query)
    author_pub_id = query.get("citation_for_view", [None])[0]
    if not author_pub_id:
        continue

    paper_citation_match = re.search(
        r'<a(?=[^>]*class="[^"]*gsc_a_ac[^"]*")[^>]*>(\d*)</a>', row
    )
    paper_citations = paper_citation_match.group(1) if paper_citation_match else ""
    publications[author_pub_id] = {
        "author_pub_id": author_pub_id,
        "num_citations": int(paper_citations) if paper_citations else 0,
        "bib": {"title": unescape(re.sub(r"<[^>]+>", "", title)).strip()},
    }

author = {
    "scholar_id": scholar_id,
    "name": unescape(re.sub(r"<[^>]+>", "", name_match.group(1))).strip(),
    "citedby": int(citation_match.group(1).replace(",", "")),
    "publications": publications,
    "updated": datetime.now(timezone.utc).isoformat(),
}

print(json.dumps(author, indent=2, ensure_ascii=False))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
