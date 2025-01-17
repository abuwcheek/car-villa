from django.urls import path
from .views import UserRegisterView, LoginView


app_name = 'users'
urlpatterns = [
    path('user-register', UserRegisterView.as_view(), name='register'),
    path('user-login', LoginView.as_view(), name='login'),
]