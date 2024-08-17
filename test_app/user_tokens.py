from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


def get_user_tokens(user):
    refresh = RefreshToken.for_user(user)
    return [str(refresh), str(refresh.access_token)]