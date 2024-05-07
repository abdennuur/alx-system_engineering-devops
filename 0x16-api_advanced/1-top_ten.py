#!/usr/bin/python3
"""
queries Reddit API and print the title of the
first 10 hot posts listed for given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API
    - If not valid subreddit, None.
    """
    reQ = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if reQ.status_code == 200:
        for get_dt in reQ.json().get("data").get("children"):
            dt = get_dt.get("data")
            title = dt.get("title")
            print(title)
    else:
        print("None")
