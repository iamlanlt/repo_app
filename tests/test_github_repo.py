from django.test import TestCase, Client
from rest_framework import status
from unittest.mock import patch
import requests

class GitHubRepoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_username = "octocat"
        self.invalid_username = "invalid_username"
        self.url = "/get-repos/"

    # Test 1: Valid username
    @patch('requests.get')
    def test_valid_username(self, mock_get):
        mock_response = [
            {"name": "repo1", "html_url": "https://github.com/octocat/repo1"},
            {"name": "repo2", "html_url": "https://github.com/octocat/repo2"}
        ]
        mock_get.return_value.status_code = status.HTTP_200_OK
        mock_get.return_value.json.return_value = mock_response

        response = self.client.get(self.url, {"username": self.valid_username})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("repos", response.json())
        self.assertEqual(len(response.json()["repos"]), 2)

    # Test 2: Missing username
    def test_missing_username(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()["error"], "Username is required")

    # Test 3: Invalid username
    @patch('requests.get')
    def test_invalid_username(self, mock_get):
        mock_get.return_value.status_code = status.HTTP_404_NOT_FOUND
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

        response = self.client.get(self.url, {"username": self.invalid_username})
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.json()["error"], "Failed to fetch data from GitHub. Please try again later.")

    # Test 4: GitHub API failure
    @patch('requests.get')
    def test_github_api_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        response = self.client.get(self.url, {"username": self.valid_username})
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.json()["error"], "Failed to fetch data from GitHub. Please try again later.")
