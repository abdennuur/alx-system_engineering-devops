import requests

def number_of_subscribers(subreddit):
    """Queries Reddit API and returns the number of subscribers for a given subreddit."""
    # Input validation
    if not subreddit or not isinstance(subreddit, str):
        raise ValueError("Subreddit name must be a non-empty string.")

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        print(f"Failed to fetch data for subreddit '{subreddit}'. Error: {response.text}")
        return 0
