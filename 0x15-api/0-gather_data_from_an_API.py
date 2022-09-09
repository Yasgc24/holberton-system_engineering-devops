#!/usr/bin/python3
"""Script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    with requests.session() as session:
        response_tasks = session.get(todos_url)
        response_users = session.get(user_url)
        data_tasks = response_tasks.json()
        data_users = response_users.json()
        name_user = data_users["name"]
        tasks_done = 0
        total_tasks = len(data_tasks)
        tasks_title = ""
        for record in data_tasks:
            if record["completed"]:
                tasks_done += 1
                tasks_title += "\t {}\n".format(record["title"])

        print("Employee {0} is done with tasks({1}/{2}):\n{3}".format(
            name_user, tasks_done, total_tasks, tasks_title), end="")
