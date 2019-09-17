#!/usr/bin/python3
""" gets all employees in the database and saves as a json"""
import json
import requests


if __name__ == "__main__":
    with open("todo_all_employees.json", 'w') as json_file:
        d = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
        u = requests.get("https://jsonplaceholder.typicode.com/users/").json()
        outer_dict = {}
        for uid in u:
            my_id = uid.get("id")
            my_list = []
            for my_dict in d:
                if my_dict.get("userId") == my_id:
                    inner_dict = {}
                    inner_dict["username"] = uid.get("username")
                    inner_dict["task"] = my_dict.get("title")
                    inner_dict["completed"] = my_dict.get("completed")
                    my_list.append(inner_dict)
            outer_dict["{}".format(my_id)] = my_list
            print(my_list)
        results = outer_dict
        json.dump(results, json_file)
