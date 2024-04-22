#!/usr/bin/python3
"""
To gathers data from API
"""

import requests
import sys


def gather_data(employee_id):
    """
    Gathers data from the given employee ID and prints TODO list progress
    """
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    todo_response = requests.get(url + "todos", params={"userId": employee_id})

    if user_response.status_code != 200:
        print("Error: User data not found")
        return
    if todo_response.status_code != 200:
        print("Error: TODO list not found")
        return
    user = user_response.json()
    todo_data = todo_response.json()

    done_tasks = [task for task in todo_data if task.get("completed")]
    total_tasks = len(todo_data)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), total_tasks
    ))
    for task in done_tasks:
        print("\t{}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    gather_data(employee_id)
