#!/usr/bin/python3
"""
function that queries the Reddit API and
returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """no. of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    # if resp.status_code != 200:
    #     return 0
    # else:
    #     return resp.json()["data"]["subscribers"]
    if resp.status_code == 200:
        try:
            return resp.json()['data']['subscribers']
        except KeyError:
            pass
    return 0
