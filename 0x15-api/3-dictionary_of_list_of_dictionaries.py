#!/usr/bin/python3
"""To exports to-do ls info of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usrs = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            us.get("id"): [{
                "task": td.get("title"),
                "completed": td.get("completed"),
                "username": us.get("username")
            } for td in requests.get(url + "todos",
                                    params={"userId": us.get("id")}).json()]
            for us in usrs}, jsonfile)
