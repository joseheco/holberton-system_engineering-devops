#!/usr/bin/python3
"""python script , use REST API"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(url).json().get('name')

    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])
    todos = requests.get(url_todos).json()
    value = [{'task': todo.get('title'), 'completed':
             todo.get('completed'), 'username': employee} for todo in todos]
    datos = {argv[1]: value}

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(datos, f)
