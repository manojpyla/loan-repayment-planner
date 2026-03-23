"""
Web Scraper — scrapes a webpage and exports structured data to XML.

Usage:
    python web_scraper.py <URL> [--output FILE]

Examples:
    python web_scraper.py https://example.com
    python web_scraper.py https://example.com --output result.xml
"""

import argparse
import sys
from xml.etree.ElementTree import Element, SubElement, ElementTree, indent

import requests
from bs4 import BeautifulSoup


def scrape(url: str) -> dict:
    """Fetch the page and extract structured content."""
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "title": soup.title.string.strip() if soup.title and soup.title.string else "",
        "meta": [],
        "headings": [],
        "paragraphs": [],
        "links": [],
        "images": [],
        "tables": [],
    }

    # Meta tags
    for tag in soup.find_all("meta"):
        name = tag.get("name") or tag.get("property", "")
        content = tag.get("content", "")
        if name and content:
            data["meta"].append({"name": name, "content": content})

    # Headings (h1–h6)
    for level in range(1, 7):
        for tag in soup.find_all(f"h{level}"):
            text = tag.get_text(strip=True)
            if text:
                data["headings"].append({"level": str(level), "text": text})

    # Paragraphs
    for tag in soup.find_all("p"):
        text = tag.get_text(strip=True)
        if text:
            data["paragraphs"].append(text)

    # Links
    for tag in soup.find_all("a", href=True):
        text = tag.get_text(strip=True)
        data["links"].append({"href": tag["href"], "text": text})

    # Images
    for tag in soup.find_all("img"):
        data["images"].append({
            "src": tag.get("src", ""),
            "alt": tag.get("alt", ""),
        })

    # Tables
    for table in soup.find_all("table"):
        rows = []
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all(["th", "td"])]
            if cells:
                rows.append(cells)
        if rows:
            data["tables"].append(rows)

    return data


def build_xml(data: dict, url: str) -> Element:
    """Convert scraped data dict into an XML ElementTree root."""
    root = Element("scraped_data", url=url)

    SubElement(root, "title").text = data["title"]

    # Meta
    if data["meta"]:
        meta_el = SubElement(root, "meta_tags")
        for m in data["meta"]:
            tag = SubElement(meta_el, "meta", name=m["name"])
            tag.text = m["content"]

    # Headings
    if data["headings"]:
        headings_el = SubElement(root, "headings")
        for h in data["headings"]:
            tag = SubElement(headings_el, "heading", level=h["level"])
            tag.text = h["text"]

    # Paragraphs
    if data["paragraphs"]:
        paras_el = SubElement(root, "paragraphs")
        for p in data["paragraphs"]:
            SubElement(paras_el, "p").text = p

    # Links
    if data["links"]:
        links_el = SubElement(root, "links")
        for lnk in data["links"]:
            tag = SubElement(links_el, "link", href=lnk["href"])
            tag.text = lnk["text"]

    # Images
    if data["images"]:
        imgs_el = SubElement(root, "images")
        for img in data["images"]:
            SubElement(imgs_el, "image", src=img["src"], alt=img["alt"])

    # Tables
    if data["tables"]:
        tables_el = SubElement(root, "tables")
        for i, table_rows in enumerate(data["tables"]):
            table_el = SubElement(tables_el, "table", id=str(i + 1))
            for row in table_rows:
                row_el = SubElement(table_el, "row")
                for cell in row:
                    SubElement(row_el, "cell").text = cell

    return root


def main():
    parser = argparse.ArgumentParser(description="Scrape a webpage and export to XML.")
    parser.add_argument("url", nargs="?", default=None, help="URL of the webpage to scrape")
    parser.add_argument("--output", "-o", default="scraped_data.xml",
                        help="Output XML file path (default: scraped_data.xml)")
    args = parser.parse_args()

    url = args.url if args.url else input("Enter the URL to scrape: ").strip()
    if not url:
        print("Error: No URL provided.", file=sys.stderr)
        sys.exit(1)

    output_file = args.output
    if output_file == "scraped_data.xml":
        user_output = input("Enter the output XML file name (default: scraped_data.xml): ").strip()
        if user_output:
            output_file = user_output if user_output.endswith(".xml") else user_output + ".xml"

    print(f"Scraping: {url}")
    try:
        data = scrape(url)
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)

    root = build_xml(data, url)
    indent(root, space="  ")

    tree = ElementTree(root)
    tree.write(output_file, encoding="unicode", xml_declaration=True)
    print(f"Saved to: {output_file}")

    # Print summary
    print(f"\n--- Summary ---")
    print(f"  Title:      {data['title']}")
    print(f"  Meta tags:  {len(data['meta'])}")
    print(f"  Headings:   {len(data['headings'])}")
    print(f"  Paragraphs: {len(data['paragraphs'])}")
    print(f"  Links:      {len(data['links'])}")
    print(f"  Images:     {len(data['images'])}")
    print(f"  Tables:     {len(data['tables'])}")


if __name__ == "__main__":
    main()
