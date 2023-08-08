#!/usr/bin/env bash

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    Args:
    subreddit (str): The name of the subreddit to query.
    Returns:
    int: The number of subscribers for the given subreddit. If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Custom User Agent'  # Set your custom User-Agent here
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
if __name__ == '__main__':
    subreddit = input("Enter the name of the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"The number of subscribers for /r/{subreddit} is {subscribers}")
