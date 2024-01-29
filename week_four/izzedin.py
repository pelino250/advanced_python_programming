# TODO: Import the necessary libraries
# You will need the 'requests' library and 'HTTPBasicAuth' from 'requests.auth'
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import os

load_dotenv()


def basic_auth():
    email = os.environ.get("IZZEDDIN_EMAIL")
    password = os.environ.get("IZZEDDIN_PASSWORD")
    username = os.environ.get("IZZEDDIN_USERNAME")
    auth = HTTPBasicAuth(email, password)
    try:
        response = requests.get(f"https://api.github.com/{username}", auth=auth)
        print(response.json())
    except Exception as e:
        print(e)


basic_auth()
# TODO: secure your credentials in .env
#

# TODO: Make a GET request to 'https://api.github.com/user' using basic authentication
# Use the 'requests.get()' function and pass in the URL and your credentials
# Your credentials should be passed to the 'auth' parameter as an instance of 'HTTPBasicAuth'

# TODO: Print the response
# Use the '.json()' method of the response object to print the response in JSON format

# TODO: Handle possible exceptions
# Wrap your code in a try-except block to handle possible exceptions, such as a 'requests.exceptions.RequestException'

""" Here's the skeleton of the code you need to fill:"""
# import requests
# from requests.auth import HTTPBasicAuth
#
# def basic_auth():
#     try:
#         # TODO: Fill in your code here
#     except requests.exceptions.RequestException as e:
#         print(e)
#
# basic_auth()
