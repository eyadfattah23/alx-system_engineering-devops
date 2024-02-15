#!/usr/bin/python3
'''
 function that queries the Reddit API and returns the number of subscribers
 (not active users, total subscribers)
 for a given subreddit.
 If an invalid subreddit is given, the function should return 0.
'''
import requests

base_url = 'https://oauth.reddit.com'


def number_of_subscribers(subreddit):
    '''queries the Reddit API and returns the number of subscribers'''

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers
