# This Script returns the names and visibility of a users repositories.
# The main takeaway from this is the process of requesting from the api using the 
# requests library.
# The main things that will change are the URL and output data handling.

# This script requires a .env file containing a USERNAME and TOKEN
# A personal access token can be generated on Github

import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

token = os.getenv('TOKEN')
username = os.getenv('USERNAME')

# Gets Private Repos
url = f"https://api.github.com/search/repositories?q=user:{username}"

headers = {"Authorization": "token " + token}

response = requests.get(url=url, headers=headers)
data = response.json()

# Prints formatted JSON
# pprint(data)

# Prints all the keys in the Dictionary
# for key, value in data.items():
#     print(key)

repos = data["items"]

for repo in repos:
    print(f"Name: {repo["name"]} | Visibility: {repo["visibility"]}")