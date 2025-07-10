# Twitter FollowerScraper

A command-line tool to scrape followers from a public X (formerly Twitter) profile using the legacy X API.

---

## 📦 Features

- Scrapes followers of a given X (Twitter) username.
- Automatically handles pagination via cursors.
- Retries on failed requests (with exponential backoff).
- Saves followers to a `.txt` file.
- Color-coded terminal interface.
- Windows/Linux console title support.

---

## ⚙️ Requirements

- Python 3.7+
- Modules:
  - `requests`
  - `colorama`

Install dependencies using:

```bash
pip install -r requirements.txt
