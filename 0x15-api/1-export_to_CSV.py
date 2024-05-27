#!/usr/bin/python3
'''script that uses REST API,
for a given employee ID,
to return information about his/her todo list progress.
and export to a csv file USER_ID.csv'''

import requests
from sys import argv
import csv

if __name__ == "__main__":
    user_id = int(argv[1])
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos/').json()

    userName = user.get('username')
    with open(f'{user_id}.csv', 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task.get('userId') == user_id:
                writer.writerow([str(user_id), userName, str(
                    task.get('completed')), task.get('title')])
