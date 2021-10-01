#!/usr/bin/python3
"""Module for task 2"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Reddit API and returns all hot postst"""

    info = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        params={"count": count, "after": after},
                        headers={"User-Agent": "Custom"},
                        allow_redirects=False)
    if info.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in info.json()
                        .get("data")
                        .get("children")]

    info_l = info.json()
    if not info_l.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info_l.get("data").get("count"),
                   info_l.get("data").get("after"))
