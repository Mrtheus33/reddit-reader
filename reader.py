"""Read-only digest of top posts and comments from a few subreddits."""

import os

import praw
from dotenv import load_dotenv

SUBREDDITS = ["AskReddit", "technology", "worldnews", "brasil"]
POSTS_PER_SUBREDDIT = 10
COMMENTS_PER_POST = 5


def main():
    load_dotenv()
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent=os.environ["REDDIT_USER_AGENT"],
    )
    reddit.read_only = True

    for name in SUBREDDITS:
        print(f"\n===== r/{name} =====")
        for post in reddit.subreddit(name).top(time_filter="day", limit=POSTS_PER_SUBREDDIT):
            print(f"\n[{post.score}] {post.title}\n{post.url}")
            post.comment_sort = "top"
            post.comments.replace_more(limit=0)
            for comment in post.comments[:COMMENTS_PER_POST]:
                print(f"  - {comment.body[:200]!r}")


if __name__ == "__main__":
    main()
