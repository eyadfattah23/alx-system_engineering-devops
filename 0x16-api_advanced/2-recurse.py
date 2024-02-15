#!/usr/bin/python3
'''recursive function that queries the Reddit API,
returns a list containing the titles of all hot articles
for a given subreddit.
If no results are found for the given subreddit,
the function should return None.'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''returns a list containing the titles of all hot articles'''

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?\
        limit=100&after={after}'
    headers = {'User-Agent': 'myapp/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return None

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        aft = data["data"]["after"]
        if not aft:
            return hot_list
    else:
        return None
    if not ("data" in data) and not ("after" in data["data"]):
        return hot_list
    return recurse(subreddit, hot_list, aft)
