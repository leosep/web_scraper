import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve
from utils.logger import log

def download_file(file_url, file_path):
    try:
        urlretrieve(file_url, file_path)
        log(f"Downloaded: {file_url}")
    except Exception as e:
        log(f"Error downloading {file_url}: {e}", error=True)

def process_page(page_url, download_folder, visited_urls):
    try:
        response = requests.get(page_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        log(f"Error fetching {page_url}: {e}", error=True)
        return

    soup = BeautifulSoup(response.content, "html.parser")

    # Download and rewrite assets
    asset_types = {
        "img": ("src", "images"),
        "link": ("href", "css"),
        "script": ("src", "js")
    }

    for tag, (attr, folder) in asset_types.items():
        for node in soup.find_all(tag):
            asset_url = node.get(attr)
            if not asset_url or (tag == "link" and node.get("rel") != ["stylesheet"]):
                continue
            abs_url = urljoin(page_url, asset_url)
            file_name = os.path.basename(urlparse(abs_url).path)
            file_path = os.path.join(download_folder, folder, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            download_file(abs_url, file_path)
            node[attr] = os.path.join(folder, file_name)

    # Save modified HTML
    page_name = os.path.basename(urlparse(page_url).path) or "index.html"
    page_path = os.path.join(download_folder, page_name)
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    # Recursively download linked pages
    for link in soup.find_all("a", href=True):
        next_url = urljoin(page_url, link["href"])
        if next_url.startswith(page_url) and next_url not in visited_urls:
            visited_urls.add(next_url)
            process_page(next_url, download_folder, visited_urls)
