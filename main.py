import argparse
from scraper.downloader import download_site

def main():
    parser = argparse.ArgumentParser(description="Download a website locally.")
    parser.add_argument("url", help="The URL to download.")
    parser.add_argument("output", help="Output folder to store the website.")
    args = parser.parse_args()

    download_site(args.url, args.output)

if __name__ == "__main__":
    main()
