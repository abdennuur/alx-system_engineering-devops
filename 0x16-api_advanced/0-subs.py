#!/usr/bin/python3
"""To queries Reddit API and return the number of subscribers
for given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """queries Reddit API and return number of
    subscribers for given subreddit"""
    uRl = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    resP = requests.get(uRl, headers=headers)
    if resP.status_code == 200:
        data = resP.json()
        return data.get('data').get('subscribers')
    else:
        return 0
