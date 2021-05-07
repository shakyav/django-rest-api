from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from code_snippets import views

urlpatterns = [
    path('code_snippets/', views.SnippetList.as_view(),name='snippet-list'),
    path('code_snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'),
    path('users/', views.UserList.as_view(),name='user-list'), # new
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'), # new
    path('', views.api_root), # branch api root endpoint
]

urlpatterns = format_suffix_patterns(urlpatterns)