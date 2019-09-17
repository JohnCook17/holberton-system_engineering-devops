#!/usr/bin/python3
""" gets data from api and saves as json """
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    with open("{}.json".format(employee_id), 'w') as json_file:
        data = requests.get("https://jsonplaceholder.typicode.com/todos/",
                            params={"userId": employee_id}).json()
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id)).json()
        name = user.get("username")
        my_list = []
        for my_dict in data:
            empty_dict = {}
            for _ in my_dict.values():
                empty_dict["task"] = my_dict.get("title")
                empty_dict["completed"] = my_dict.get("completed")
                empty_dict["username"] = name
            my_list.append(empty_dict)
        results = {}
        results["{}".format(employee_id)] = my_list
        json.dump(results, json_file)
