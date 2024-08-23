#!/usr/bin/python3
"""new"""

import requests


def count_words(subreddit, word_list, word_dic={}, nex=None):
    """count word"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-user'}
    params = {'limit': 100, 'after': nex}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        for i in range(100):
            title = response.json()["data"]["children"][i]["data"]["title"]
            for word in word_list:
                if word.lower() in title.lower():
                    if word in word_dic:
                        word_dic[word] += 1
                    else:
                        word_dic[word] = 1
        nex = response.json()["data"]["after"]
        if nex is None:
            for m, value in sorted(word_dic.items(),
                                   key=lambda x: (-x[1], x[0])):
                if value != 0:
                    print("{}: {}".format(m, value))
            return
        return count_words(subreddit, word_list, nex, word_dic)
