from django.urls import path
from .views import UserRegisterView, LoginView, UserProfileView, UpdateUserView


app_name = 'users'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='myprofile'),
    path('profile-update/', UpdateUserView.as_view(), name='updateuser'),
]