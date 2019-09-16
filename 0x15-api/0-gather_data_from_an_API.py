#!/usr/bin/python3
import requests
import sys
import json

employee_id = sys.argv[1]
data = requests.get("https://jsonplaceholder.typicode.com/todos/", params={"userId": employee_id}).json()
user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
task_done = 0
total_task = 0
name = user.get("name")
total_task = len(data)
for my_dict in data:
    task_status = my_dict.get("completed")
    if task_status == True:
        task_done += 1
print("Employee {} is done with tasks({}/{}):".format(name, task_done, total_task))
for my_dict in data:
    if my_dict.get("completed") == True:
        print("\t {}".format(my_dict.get("title")))
