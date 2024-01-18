import requests


def fetch_repos(username, page=None, per_page=None):
    # TODO: Implement pagination by using the 'page' and 'per_page' parameters in the API request. The 'page'
    #  parameter specifies the page number and the 'per_page' parameter specifies the number of items per page. For
    #  example, to fetch the first page with 10 items, you would set 'page' to 1 and 'per_page' to 10.

    # Define the base URL
    base_url = f"https://api.github.com/users/{username}/repos"

    # Send the request
    response = requests.get(base_url)

    # Parse the response
    repos = response.json()


    # TODO: Print the number of repos fetched and the current page number.
    # This will help in verifying that the pagination is working correctly.


    # Print the repos
    for repo in repos:
        print(repo['name'])


# Fetch all repos without pagination
# fetch_repos('ipelino')

# TODO: Call the 'fetch_repos' function with different page numbers and per_page values to test the pagination.
# For example, you could fetch the first page with 10 items, then the second page with 10 items, and so on.
fetch_repos('ipelino', page=1, per_page=5)