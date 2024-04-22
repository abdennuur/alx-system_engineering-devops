#!/usr/bin/python3
"""Exports TODO list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = requests.get(url + "todos", params={"userId": user_id}).json()
        all_tasks[user_id] = [{"task": task.get("title"),
                               "completed": task.get("completed"),
                               "username": username} for task in tasks]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
