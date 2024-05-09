#!/usr/bin/python3
"""
TO queries subscribers on given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if response is a redirection indicating a non-existing subreddit
    if response.status_code == 302:
        return 0

    # To Check if response is successful and retrieve the subscriber count
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers

    # Return -> 0 for any other cases (e.g., errors)
    return 0
