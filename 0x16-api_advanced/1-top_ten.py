#!/usr/bin/python3
''' function that queries the Reddit API
prints the titles of the first 10 hot post
listed for a given subreddit.'''
import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot post'''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {
        'User-Agent': 'myapp/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
    data = response.json()['data']['children']
    for post in data:
        print(post['data']['title'])
