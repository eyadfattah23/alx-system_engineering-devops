#!/usr/bin/python3
''' function that queries the Reddit API
prints the titles of the first 10 hot post
listed for a given subreddit.'''

import requests

'''url = 'https://www.reddit.com/r/programming/about.json'

r = requests.get(url, auth=('L6IfrPbBUX5qkFAj4MqLdg',
                 'TwZviLWscqEJgWQ0PRYfmgOy_T03NA'))

print(r.json()['data']['subscribers'])
'''


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts'''

    URL = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if not subreddit:
        print(None)
        return

    headers = {
        'User-Agent':
        'api_advanced_eyad22 by Practical_County_194 (personal use script)'
    }

    try:
        r = requests.get(URL, headers=headers, timeout=10)

        if r.status_code != 200:
            print(f"Error: Received status code {r.status_code}")
            print(None)
            return

        try:
            data = r.json()
        except ValueError:
            # Print the actual response for debugging if JSON decoding fails
            print(f"Error: Unable to parse JSON. Response content: {r.text}")
            print(None)
            return

        # Extract and print titles of the first 10 hot posts
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return

        for i, post in enumerate(posts[:10]):
            print(post.get('data', {}).get('title'))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print(None)
