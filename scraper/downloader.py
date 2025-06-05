import os
from urllib.parse import urlparse
from .processor import process_page

def download_site(url, download_folder):
    os.makedirs(download_folder, exist_ok=True)
    visited_urls = set()
    visited_urls.add(url)
    process_page(url, download_folder, visited_urls)
