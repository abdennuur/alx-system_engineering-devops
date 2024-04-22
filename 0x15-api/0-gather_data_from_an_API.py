#!/usr/bin/python3
"""To returns -> to-do list info for given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        usr.get("name"), len(done), len(todo)))
    [print("\t {}".format(c)) for c in done]
