import requests
# Function to fetch pull requests from GitHub
def fetch_pull_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')
        return None
# Function to count PR creators   
def count_pr_creators(pull_requests):
    pr_creators = {}
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1
    return pr_creators

# Function to display PR creator count
def display_pr_creators(pr_creators):
    print("PR Creators and Count")
    for creator, count in pr_creators.items():
        print(f'{creator}: {count} PR(s)')

# Main function to control the flow
def main():
    url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
    pull_requests = fetch_pull_request(url)
    if pull_requests:
        pr_creators = count_pr_creators(pull_requests)
        display_pr_creators(pr_creators)

# Entry point
if __name__ == "__main__":
    main()
