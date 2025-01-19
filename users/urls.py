from django.urls import path
from .views import UserRegisterView, LoginView, UserProfileView, UpdateUserView


app_name = 'users'
urlpatterns = [
    path('user-register', UserRegisterView.as_view(), name='register'),
    path('user-login', LoginView.as_view(), name='login'),
    path('user-profile', UserProfileView.as_view(), name='myprofile'),
    path('user-update', UserProfileView.as_view(), name='updateuser'),
]