from tkinter.font import names

from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from main import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path("main/", views.SnippetList.as_view(), name='snippet-list'),
    path("<int:pk>/", views.SnippetDetail.as_view(), name='snippet-detail'),
    path('<int:pk>/highlight/', views.SnippetHighLight.as_view(), name='snippet-highlight'),
    path("users/", views.UserList.as_view(),
         name='user-list'),
    path("users/<int:pk>/", views.UserDetail.as_view(),
         name='user-detail'),
])

