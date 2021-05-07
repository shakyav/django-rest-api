from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from code_snippets import views

urlpatterns = [
    path('code_snippets/', views.SnippetList.as_view()),
    path('code_snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)