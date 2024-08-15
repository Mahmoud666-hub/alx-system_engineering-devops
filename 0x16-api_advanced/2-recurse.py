#!/usr/bin/python3
"""returns a list containing the titles of all hot articles"""

import requests


def recurse(subreddit, hot_list=[]):
    """recursion"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python-requests/2.32.3"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        for dat in range(10):
            title = resp.json()["data"]["children"][dat]["data"]["title"]
            hot_list.append(title)
        return hot_list
    else:
        return None
