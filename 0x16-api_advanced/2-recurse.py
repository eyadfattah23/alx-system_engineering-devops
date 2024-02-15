#!/usr/bin/python3
'''recursive function that queries the Reddit API,
returns a list containing the titles of all hot articles
for a given subreddit.
If no results are found for the given subreddit,
the function should return None.'''
import requests


def recurse(subreddit, hot_list=[], limit=100, page_number=1):
    '''returns a list containing the titles of all hot articles'''

    if len(hot_list) >= limit:  # Limiting the number of posts
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"page": page_number}
    headers = {'User-Agent': 'myapp/1.0'}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return None

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

    if "data" in data and "after" in data["data"]:
        page_num = page_number
        page_num += 1
        return recurse(subreddit, hot_list, page_number=page_num)
    return hot_list
