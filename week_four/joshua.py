# TODO: Import the necessary libraries
# You will need the 'requests' library and 'HTTPBasicAuth' from 'requests.auth'

# TODO: Define your username and password
# These are the credentials you will use for basic authentication

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
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: Define your username and password
# These are the credentials you will use for basic authentication
username = os.getenv('Jbizima02@github.com')
password = os.getenv('I will not share it !!')

def basic_auth():
    try:
        # TODO: Make a GET request to 'https://api.github.com/user' using basic authentication
        # Use the 'requests.get()' function and pass in the URL and your credentials
        # Your credentials should be passed to the 'auth' parameter as an instance of 'HTTPBasicAuth'
        response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username, password))

        # TODO: Print the response
        # Use the '.json()' method of the response object to print the response in JSON format
        print(response.json())

    except requests.exceptions.RequestException as e:
        print(e)

# Call the function to execute the code
basic_auth()

