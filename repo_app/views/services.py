import logging
import requests

logger = logging.getLogger('django')

def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()

        if not repos:
            return True, []

        return True, [{'name': repo['name'], 'url': repo['html_url']} for repo in repos]

    except requests.exceptions.RequestException as e:
        logger.error(f"GitHub API error for user {username}: {e}")
        return False, "Failed to fetch data from GitHub. Please try again later."
