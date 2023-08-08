#!/usr/bin/env bash

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.
    Args:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): A list to store the titles of hot articles (default is an empty list).
    after (str): A token to paginate through the results (default is None).
    Returns:
    list: A list containing the titles of all hot articles in the subreddit. If no results are found, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {
        'limit': 100,  # Number of items per page
        'after': after  # Pagination token
    }
    headers = {
            'User-Agent': 'Custom User Agent'  # Set your custom User-Agent here
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return hot_list
        hot_list.extend([post['data']['title'] for post in posts])
        after = data['data']['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
if __name__ == '__main__':
    subreddit = input("Enter the name of the subreddit: ")
    hot_titles = recurse(subreddit)
    if hot_titles is None:
        print("No results found for the given subreddit.")
    else:
        print("Hot article titles in /r/{subreddit}:\n")
        for i, title in enumerate(hot_titles, start=1):
            print(f"{i}. {title}")
