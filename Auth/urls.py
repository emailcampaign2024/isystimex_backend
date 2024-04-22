from django.urls import path
from .views import UserListCreateView, RoleListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('roles/', RoleListCreateView.as_view(), name='role-list'),
]
