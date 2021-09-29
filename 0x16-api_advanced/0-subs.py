#!/usr/bin/python3
"""Write function that queries the Reddit API
    and return the number of subcribers.
"""

import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers"""
    info = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit), headers={'User-Agent': 'Custom'},
                        allow_redirects=False)
    if info.status_code == 200:
        return info.json().get('data').get('subscribers')
    return 0
