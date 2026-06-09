# ReconSpider

A Python web scraping and crawling toolkit built with BeautifulSoup and Requests. Includes link extraction experiments and a depth-limited BFS crawler.

## Contents

| File | Description |
|------|-------------|
| `reconSpider.ipynb` | Main crawler notebook — BFS crawl with status codes, headers, cookies |
| `beautifulsoop.ipynb` | BeautifulSoup exploration — parsing, link extraction |
| `draft.py` / `practice.py` | Standalone scraping scripts |

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

**Run the crawler (notebook):**

Open `reconSpider.ipynb` and run all cells. By default it crawls `http://books.toscrape.com` to depth 2.

To change the target:

```python
crawler = Crawler("https://your-target.com", max_depth=2)
results = crawler.crawl()
```

**Crawler output includes:**
- URL and final URL (after redirects)
- HTTP status code
- Content-Type and response headers
- Cookies set per page
- Redirect chain

## How it works

The `Crawler` class performs a breadth-first traversal from a seed URL, staying within the same domain. At each page it extracts all `<a href>` links, resolves them to absolute URLs, and queues them if not yet visited. Crawl depth is bounded by `max_depth`.

> Intended for authorised use on sites you own or have permission to crawl (e.g. `books.toscrape.com` is a public sandbox for scraping practice).
