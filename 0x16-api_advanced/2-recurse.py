#!/usr/bin/python3
"""
The recursive function to queries Reddit API and returna list
containing titles of all hot articles for given subreddit.
If no results found for given subreddit, return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    TO queries Reddit API and return a list
    containing titles of all hot articles
    for a given subreddit.

    - If not valid subreddit, return None.
    """
    reQ = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if reQ.status_code == 200:
        for get_data in reQ.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = reQ.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
