from django.contrib import admin
from django.urls import path
from .views import UserCreateAPIView, Logout
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name=None),
    path('login/', obtain_auth_token, name='api_login'),
    path('logout/', Logout.as_view(), name=None)
]
