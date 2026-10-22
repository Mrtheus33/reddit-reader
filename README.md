# reddit-reader

Personal, non-commercial, **read-only** tool that fetches public posts and comments
from a few subreddits and summarizes them for my own use.

## What it does

- Reads the top posts of the day from a short list of subreddits (e.g. `r/AskReddit`, `r/technology`).
- Reads the top comments of each post.
- Prints a plain-text digest locally.

## What it does NOT do

- Does not post, comment, vote, or send messages.
- Does not store data long-term, resell it, or use it to train AI models.
- Does not collect personal information about users.

## Rate of use

At most a few dozen requests per hour, well below Reddit's API limits.
Uses a descriptive User-Agent, as required by Reddit's API rules.

## Setup

```bash
pip install -r requirements.txt
copy .env.example .env   # then fill in your credentials
python reader.py
```

## Compliance

This project follows Reddit's Responsible Builder Policy, Developer Terms and Data API Terms.
