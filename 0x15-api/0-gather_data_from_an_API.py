#!/usr/bin/python3
"""python script , use REST API"""

if __name__ == "__main__":
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(url).json().get('name')

    url_todos = 'https://jsonplaceholder.typicode.com/todos'.format(
        argv[1])
    todos = requests.get(url_todos).json()
    done = [todo for todo in todos if todo.get('completed')]
    print("Employee {} is done with tasks({}/{}):".format(
        employee, len(done), len(todos)))
    for a in done:
        print("\t ", a.get('title'))
