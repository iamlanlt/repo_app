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

        repo_data = []
        for repo in repos:
            languages_url = repo.get('languages_url')
            languages_response = requests.get(languages_url)
            languages_response.raise_for_status()
            languages = list(languages_response.json().keys())

            repo_data.append({
                'name': repo.get('name', 'N/A'),
                'url': repo.get('html_url', '#'),
                'description': repo.get('description', 'No description available'),
                'stars': repo.get('stargazers_count', 0),
                'forks': repo.get('forks_count', 0),
                'languages': ', '.join(languages) if languages else 'Unknown',
                'created_at': repo.get('created_at', 'Unknown'),
                'updated_at': repo.get('updated_at', 'Unknown'),
            })

        return True, repo_data

    except requests.exceptions.RequestException as e:
        logger.error(f"GitHub API error for user {username}: {e}")
        return False, "Failed to fetch data from GitHub. Please try again later."
