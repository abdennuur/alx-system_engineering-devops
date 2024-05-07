#!/usr/bin/python3
"""
To count words in all hot posts of given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function to queries Reddit API, parsestitle of all
    hot articles, and print sorted count of given keywords
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        paramts["after"] = after

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    chldrn = data["data"]["children"]

    for post in chldrn:
        title = post["data"]["title"].lower()
        for wrd in word_list:
            if wrd.lower() in title:
                counts[wrd] = counts.get(wrd, 0) + title.count(wrd.lower())

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_Cnts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for wrd, count in sorted_Cnts:
            print(f"{wrd.lower()}: {count}")
