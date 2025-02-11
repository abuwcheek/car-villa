from django.urls import path
from .views import AddToSevimlilarView, FavoriteView


app_name = 'order'
urlpatterns = [
     path('add-favorite/', AddToSevimlilarView.as_view(), name="add-favorite"),
     path('favorite/', FavoriteView.as_view(), name='favorite'),
]