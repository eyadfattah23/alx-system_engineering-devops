'''script that uses REST API,
for a given employee ID,
to return information about his/her todo list progress.
and export to a csv file USER_ID.json'''

import requests
from sys import argv
import json
if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userId = int(argv[1])
    user = requests.get(url + f"users/{userId}").json()

    user_name = user.get('username')

    file_name = f"{userId}.json"
    total_tasks = 0
    done_tasks = 0

    tasks_list = []
    tasks = requests.get(url + "todos/").json()

    with open(file_name, 'w', newline='') as file:
        for task in tasks:
            if task.get('userId') == userId:
                tasks_list.append({"task": task.get('title'),
                                   "completed": task.get('completed'),
                                   "username": user_name})
        json_dict = {f"{userId}": tasks_list}
        json.dump(json_dict, file)
        pass
