#!/usr/bin/python3
"""0. How many subs?"""
import json
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    user_agent = "reddit_user"

    headers = {"User-Agent": user_agent}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        return 0

    data = request.json()["data"]
    page_list = data["children"]
    page_data = page_list[0]["data"]

    return page_data["subreddit_subscribers"]
