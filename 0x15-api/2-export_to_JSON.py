#!/usr/bin/python3
"""Script to export data in the JSON format."""
import requests
from sys import argv
import json


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    with requests.session() as session:
        tasks = session.get(todos_url).json()
        users = session.get(user_url).json()

        list_data = []
        for record in tasks:
            completed = record["completed"]
            title = record["title"]
            username = users["username"]
            data = {
                "task": title,
                "completed": completed,
                "username": username
            }
            list_data.append(data)

        text_file = "{}.json".format(argv[1])
        with open(text_file, mode="w+", encoding="utf-8") as file:
            data_id = {argv[1]: list_data}
            json.dump(data_id, file)
