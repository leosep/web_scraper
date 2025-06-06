
# Website Downloader

This Python project downloads a full website (HTML, images, CSS, JavaScript) and saves it locally, maintaining the structure of assets and internal links.

---

## Features

- Downloads HTML pages, images, CSS, and JavaScript.
- Rewrites asset links so the site works offline.
- Recursively downloads internal links.
- Structured, clean, and modular codebase.
- CLI (Command Line Interface) support with `argparse`.
- Lightweight logging system.

---

## Folder Structure

```
web_scraper/
├── main.py                      # Entry point: accepts CLI arguments
├── scraper/
│   ├── __init__.py
│   ├── downloader.py            # Initializes and starts the download process
│   └── processor.py             # Handles HTML parsing and asset downloading
├── utils/
│   ├── __init__.py
│   └── logger.py                # Basic logging helper
├── requirements.txt             # Project dependencies
└── README.md                    # Documentation (this file)
```

---

## Getting Started

### 1. Clone the Repository

### 2. Install Dependencies

Use `pip` to install required libraries:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from the command line:

```bash
python main.py <URL> <OUTPUT_FOLDER>
```

### Example:

```bash
python main.py https://cajasdeseguridad.com.do/es/ ./downloaded_site
```

This will:

- Download all HTML pages and linked internal resources.
- Store images in `downloaded_site/images/`
- Store CSS in `downloaded_site/css/`
- Store JS in `downloaded_site/js/`
- Store the HTML in the root of the output folder.

---

## How It Works

- `main.py`: Entry point. Accepts `url` and `output` as arguments.
- `downloader.py`: Sets up output folders and starts recursive downloading.
- `processor.py`:
  - Downloads HTML and parses with `BeautifulSoup`.
  - Detects and downloads `img[src]`, `link[rel=stylesheet]`, `script[src]`.
  - Rewrites all paths to point to the locally stored copies.
  - Saves the page and recursively follows internal `<a href="">` links.
- `logger.py`: Provides simple console output.

---

## Limitations

- Does not download external resources (e.g., fonts from Google CDN).
- Does not handle JavaScript-rendered content.
- Only works with websites that do not block bots/scrapers.

---

## Example Output Structure

If downloading `https://example.com`, output folder may look like:

```
downloaded_site/
├── index.html
├── about.html
├── images/
│   └── logo.png
├── css/
│   └── style.css
└── js/
    └── script.js
```

---

## License

MIT License. Use freely and contribute if you like!

---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss your idea.
