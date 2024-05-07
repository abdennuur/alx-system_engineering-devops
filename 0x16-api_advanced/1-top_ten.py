#!/usr/bin/python3
"""
To queries Reddit API and print titles of
first 10 hot posts listed for given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    TOqueries the Reddit API
    - If not a valid subreddit -> print None.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
