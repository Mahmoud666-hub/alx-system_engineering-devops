#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """titles"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Custom"}
    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        try:
            fil = resp.json()['data']['children']
        except KeyError:
            print("None")
            return
        for post in fil:
            print(post["data"]["title"])
