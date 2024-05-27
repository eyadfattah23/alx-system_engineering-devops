#!/usr/bin/python3
'''script that uses REST API,
for a given employee ID,
to return information about Records all tasks from all employees'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/').json()

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos/').json()

    users_data = {}
    for user in users:
        user_id = user.get('id')
        userName = user.get('username')
        users_data[f"{user_id}"] = []
        for task in todos:
            if task.get('userId') == user_id:
                task_dict = {
                    "username": userName,
                    "task": f"{task.get('title')}",
                    "completed": task.get('completed'),
                }

                users_data[f"{user_id}"].append(task_dict)

    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
