#!/usr/bin/env bash
import json
import requests


def number_of_subscribers(subreddit):
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    data = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers=user_agent,
                        allow_redirects=False)
    if data.status_code != 200:
        return 0
    json_data = data.json()
    results = json_data.get("data").get("subscribers")
    return results
