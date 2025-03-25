from django.urls import path
from .views import GitHubRepoView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('get-repos/', GitHubRepoView.as_view(), name='get_repos'),
]
