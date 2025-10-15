import requests

# URL to fetch pull request from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch all the pull requests data from the GitHub API
response = requests.get(url) # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their count
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1
    # Display the dictionary of PR creators and their count
    print("PR Creators and Count")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)" )
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
