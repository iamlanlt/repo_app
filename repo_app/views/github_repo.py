from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import fetch_github_repos


class IndexView(TemplateView):
    template_name = 'repo_app/index.html'


class GitHubRepoView(APIView):
    def get(self, request):
        username = request.GET.get('username')
        if not username:
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)

        success, data = fetch_github_repos(username)
        if success:
            return Response({'repos': data})
        return Response({'error': data}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
