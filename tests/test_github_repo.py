from django.test import TestCase, Client
from rest_framework import status
from unittest.mock import patch, Mock
import requests

class GitHubRepoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_username = "octocat"
        self.invalid_username = "invalid_username"
        self.url = "/get-repos/"

    # Missing username
    def test_missing_username(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()["error"], "Username is required")

    # Valid username
    @patch('requests.get')
    def test_valid_username(self, mock_get):
        mock_repos_response = [
            {
                "name": "repo1",
                "html_url": "https://github.com/octocat/repo1",
                "stargazers_count": 10,
                "forks_count": 5,
                "description": "Repo 1 description",
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-02-01T00:00:00Z",
                "languages_url": "https://api.github.com/repos/octocat/repo1/languages"
            }
        ]

        mock_languages_response = {"Python": 10000, "JavaScript": 5000}

        mock_get.side_effect = [
            Mock(status_code=200, json=lambda: mock_repos_response),
            Mock(status_code=200, json=lambda: mock_languages_response)
        ]

        response = self.client.get(self.url, {"username": self.valid_username})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("repos", response.json())
        self.assertEqual(len(response.json()["repos"]), 1)
        repo = response.json()["repos"][0]
        self.assertEqual(repo["name"], "repo1")
        self.assertEqual(repo["url"], "https://github.com/octocat/repo1")
        self.assertEqual(repo["stars"], 10)
        self.assertEqual(repo["forks"], 5)
        self.assertEqual(repo["description"], "Repo 1 description")
        self.assertEqual(repo["languages"], "Python, JavaScript")
        self.assertEqual(repo["created_at"], "2024-01-01T00:00:00Z")
        self.assertEqual(repo["updated_at"], "2024-02-01T00:00:00Z")

    # Invalid username
    @patch('requests.get')
    def test_invalid_username(self, mock_get):
        mock_get.return_value.status_code = status.HTTP_404_NOT_FOUND
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

        response = self.client.get(self.url, {"username": self.invalid_username})
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.json()["error"], "Failed to fetch data from GitHub. Please try again later.")

    # GitHub API failure
    @patch('requests.get')
    def test_github_api_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        response = self.client.get(self.url, {"username": self.valid_username})
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.json()["error"], "Failed to fetch data from GitHub. Please try again later.")
