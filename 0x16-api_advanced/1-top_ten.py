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
    '''prints the titles of the first 10 hot post'''

    URL = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    if not subreddit:
        print(None)
        return
    try:
        headers = {
            'User-Agent': 'myapp/1.0'}
        r = requests.get(URL, auth=('L6IfrPbBUX5qkFAj4MqLdg',
                                    'TwZviLWscqEJgWQ0PRYfmgOy_T03NA'),
                         headers=headers)

        if r.status_code != 200:
            print(None)
            return

        i = 0
        for post in r.json()['data']['children']:
            if i == 10:
                break
            print(post['data']['title'])
            i += 1
    except Exception as e:
        print('error: ', e)
        print(None)
