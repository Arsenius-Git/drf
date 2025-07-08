from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from main import views

urlpatterns = [
    path("main/", views.SnippetList.as_view()),
    path("<int:pk>/", views.SnippetDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
