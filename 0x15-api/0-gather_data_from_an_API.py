#!/usr/bin/python3
'''script that uses REST API,
for a given employee ID,
to return information about his/her todo list progress.'''


import requests
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()

    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos/').json()

    user_name = user.get('name')

    todos_total = 0
    todos_done = 0
    done_list = []
    for task in todos:
        if task.get('userId') == user_id:
            todos_total += 1
            if task.get('completed'):
                todos_done += 1
                done_list.append(task.get('title'))

    print(
        f'Employee {user_name} is done with tasks({todos_done}/{todos_total}):')

    for title in done_list:
        print(f'\t {title}')
