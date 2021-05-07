from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from code_snippets import views

urlpatterns = [
    path('code_snippets/', views.SnippetList.as_view()),
    path('code_snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()), # new
    path('users/<int:pk>/', views.UserDetail.as_view()), # new
]

urlpatterns = format_suffix_patterns(urlpatterns)