#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints
   the titles of the first 10 hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """Return the top 10 hot posts"""
    info = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                        .format(subreddit), headers={'User-Agent': 'Custom'},
                        allow_redirects=False)

    if info.status_code == 200:
        [print(child.get('data').get('title'))
            for child in info.json().get('data').get('children')]
    print('None')
