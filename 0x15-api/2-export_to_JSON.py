#!/usr/bin/python3
'''script that uses REST API,
for a given employee ID,
to return information about his/her todo list progress.
and export to a json file USER_ID.json'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos/').json()

    userName = user.get('username')

    user_data = {f"{user_id}": []}

    for task in todos:
        if task.get('userId') == user_id:
            task_dict = {
                "task": f"{task.get('title')}",
                "completed": task.get('completed'),
                "username": userName}

            user_data[f"{user_id}"].append(task_dict)

    with open(f'{user_id}.json', 'w') as file:
        json.dump(user_data, file)
