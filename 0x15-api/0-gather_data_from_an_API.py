#!/usr/bin/python3
'''script that uses REST API,
for a given employee ID,
to return information about his/her todo list progress.'''


import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    userId = int(argv[1])
    user = requests.get(url + f"users/{userId}").json()
    user_name = user.get('name')

    total_tasks = 0
    done_tasks = 0

    dtasks_titles = []
    tasks = requests.get(url + "todos/").json()

    for task in tasks:
        if task.get('userId') == userId:
            total_tasks += 1
            if task.get('completed') is True:
                done_tasks += 1
                dtasks_titles.append(task.get('title'))

    print("Employee {} \
    is done with tasks({}/{}):"
          .format(user_name,
                  done_tasks,
                  total_tasks))

    for title in dtasks_titles:
        print("\t {}".format(title))
