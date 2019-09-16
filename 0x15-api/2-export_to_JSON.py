#!/usr/bin/python3
import requests
import sys
import json

if __name__ == "__main__":
    with open("USER_ID.json", 'w') as json_file:
        employee_id = sys.argv[1]
        data = requests.get("https://jsonplaceholder.typicode.com/todos/",
                            params={"userId": employee_id}).json()
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id)).json()
        name = user.get("name")
        total_task = len(data)
        my_list = []
        for my_dict in data:
            for _ in list(my_dict):
                my_dict["task"] = my_dict.get("title")
                my_dict["completed"] = my_dict.get("completed")
                my_dict["username"] = name
            my_list.append(my_dict)
        results = {}
        results["{}".format(employee_id)] = my_list
        json.dump(results, json_file)
