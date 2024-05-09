#!_usr/bin/python3
"""
TO queries subscribers on given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    else:
        # If the subreddit does not exist, Reddit returns a 404 status code
        if response.status_code == 404:
            return 0
        else:
            # Handle other potential errors by printing the status code
            print("Error:", response.status_code)
            return 0
