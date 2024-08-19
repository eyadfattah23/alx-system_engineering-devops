#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""

import requests

'''url = 'https://www.reddit.com/r/programming/about.json'

r = requests.get(url, auth=('L6IfrPbBUX5qkFAj4MqLdg',
                 'TwZviLWscqEJgWQ0PRYfmgOy_T03NA'))

print(r.json()['data']['subscribers'])
'''


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers in the given subreddit'''

    URL = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    if not URL:
        return 0
    try:
        r = requests.get(URL, auth=('L6IfrPbBUX5qkFAj4MqLdg',
                                    'TwZviLWscqEJgWQ0PRYfmgOy_T03NA'))

        if r.status_code != 200:
            return 0

        return r.json()['data']['subscribers']
    except Exception as e:
        return 0
