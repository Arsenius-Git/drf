from tkinter.font import names

from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from main import views
from main.views import api_root, SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

