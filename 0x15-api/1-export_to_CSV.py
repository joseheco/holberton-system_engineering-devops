#!/usr/bin/python3
"""Python script, use REST API"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    employee = requests.get(url).json().get('username')

    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1])
    todos = requests.get(url_todos).json()
    datos = [[argv[1], employee, todo.get('completed'), todo.get('title')]
             for todo in todos]

    with open('{}.csv'.format(argv[1]), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(datos)
