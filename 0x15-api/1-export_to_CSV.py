#!/usr/bin/python3
'''gets data from api and saves to csv'''
import csv
import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    with open('{}.csv'.format(employee_id), mode='w') as uid:
        uid_writer = csv.writer(uid,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_ALL)
        data = requests.get('https://jsonplaceholder.typicode.com/todos/',
                            params={'userId': employee_id}).json()
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employee_id)).json()
        name = user.get('username')
        for my_dict in data:
            uid_writer.writerow([employee_id,
                                 name,
                                 my_dict.get('completed'),
                                 my_dict.get('title')])
