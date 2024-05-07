#!/usr/bin/python3
"""
TO queries Reddit API and return the number of subscribers
(not active users), (total subscribers) for given subreddit.
If invalid subreddit -> given, return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    To queries the Reddit API
    - return 0 -> if not a valid subreddit.
    """
    reQu = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if reQu.status_code == 200:
        return reQu.json().get("data").get("subscribers")
    else:
        return 0
