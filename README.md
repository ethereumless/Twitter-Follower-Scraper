# 🐦 Twitter Follower Scraper

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

## 🚀 Usage

`python FollowerScraper.py`
Then input the X (Twitter) username when prompted (max 15 characters). The script will:

- Scrape all followers via the legacy API

- Save them to a file named <username>_Followers.txt

---

## ⚙️ Requirements

- Python 3.7+
- Modules:
  - `requests`
  - `colorama`

Install dependencies using:

```bash
pip install -r requirements.txt
