#!/usr/bin/env bash

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    Args:
    subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'Custom User Agent'  # Set your custom User-Agent here
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if len(posts) == 0:
            print(f"No posts found in /r/{subreddit}.")
            return
        print(f"Top 10 hot posts in /r/{subreddit}:\n")
        for i, post in enumerate(posts[:10], start=1):
            print(f"{i}. {post['data']['title']}")
    else:
        print("None")
if __name__ == '__main__':
    subreddit = input("Enter the name of the subreddit: ")
    top_ten(subreddit)
