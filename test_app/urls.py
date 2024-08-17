from django.urls import path, include
from .views import LoginAPI, RegisterAPI, UserList
urlpatterns = [
	path('auth/login', LoginAPI.as_view()),
	path('auth/user-register', RegisterAPI.as_view()),
	path('auth/user-list', UserList.as_view()),
	
]
