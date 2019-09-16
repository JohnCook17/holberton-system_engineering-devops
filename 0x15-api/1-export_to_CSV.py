#!/usr/bin/python3
"""gets data from api and saves to csv"""
import csv
import json
import requests
import sys



if __name__ == "__main__":
    with open("USER_ID.csv", mode='w') as uid:
        uid_writer = csv.writer(uid,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        uid_writer.writerow(["USER_ID",
                             "USERNAME",
                             "TASK_COMPLETED_STATUS",
                             "TASK_TITLE"])
        employee_id = sys.argv[1]
        data = requests.get("https://jsonplaceholder.typicode.com/todos/",
                            params={"userId": employee_id}).json()
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id)).json()
        name = user.get("name")
        for my_dict in data:
            uid_writer.writerow(["{}".format(name),
                                 "{}".format(employee_id),
                                 "{}".format(my_dict.get("completed")),
                                 "{}".format(my_dict.get("title"))])
