#!/usr/bin/python3
'''script that uses REST API,
for a given employee ID,
to return information about his/her todo list progress.
and export to a csv file USER_ID.csv'''

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userId = int(argv[1])
    user = requests.get(url + f"users/{userId}").json()

    user_name = user.get('username')

    file_name = f"{userId}.csv"
    total_tasks = 0
    done_tasks = 0

    dtasks_titles = []
    tasks = requests.get(url + "todos/").json()

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for task in tasks:
            if task.get('userId') == userId:
                # Form:"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
                writer.writerow([f"{userId}", f"{user_name}",
                                 f"{str(task.get('completed'))}",
                                 f"{task.get('title')}"])
