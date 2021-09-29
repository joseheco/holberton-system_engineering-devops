#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints
   the titles of the first 10 hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """Return the top 10 hot posts"""
    info = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                        .format(subreddit), allow_redirects=False,
                        headers={'User-Agent': 'Custom'}).json().get(
                            'data').get('children')

    if info.status_code >= 300:
        print('None')
    else:
        for child in info:
            print(child.get('data').get('title'))
