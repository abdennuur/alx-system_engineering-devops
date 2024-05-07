#!/usr/bin/python3
"""
To query list of all hot posts on given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    TO recursively retrieves list of titles of all hot posts
    on given subreddit

    Args:
        subreddit (str): name of the subreddit.
        hot_list (list, optional): List to store post titles.
                                    Default -> empty list.
        after (str, optional): Token for pagination.
                                    Default -> empty string.
        count (int, optional): Current count of retrieved posts,
                                    Default -> 0.

    Returns:
        list: List of post titles from hot section of  subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
