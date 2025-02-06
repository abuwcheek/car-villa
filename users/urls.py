from django.urls import path
from .views import UserRegisterView, LoginView, LogoutView ,UserProfileView, UpdateUserView, PasswordChangeView


app_name = 'users'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='myprofile'),
    path('profile-update/', UpdateUserView.as_view(), name='updateuser'),
    path('password-update/', PasswordChangeView.as_view(), name='updatepassword'),
]