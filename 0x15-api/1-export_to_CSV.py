#!/usr/bin/python3
"""Script to export data in the CSV format."""
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    URL_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id)
    URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    with requests.session() as session:
        response_tasks = session.get(URL_tasks)
        response_users = session.get(URL_user)
        data_tasks = response_tasks.json()
        data_users = response_users.json()
        username = data_users["username"]
        tasks_done = 0
        tasks_all = len(data_tasks)
        data = ""
        for record in data_tasks:
            completed = record["completed"]
            title = record["title"]
            data += '"{}","{}","{}","{}"\n'.format(
                id, username, completed, title)
        textFile = "{}.csv".format(id)
        with open(textFile, mode="w+", encoding="utf-8") as file:
            file.write(data)
