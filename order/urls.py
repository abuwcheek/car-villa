from django.urls import path
from .views import AddToFavoriteView, FavoriteListView, RemoveProductInFavoriteView, AddToShopCartView



app_name = 'order'
urlpatterns = [
     path('order-to-favorite/', AddToFavoriteView.as_view(), name='addtofavorite'),
     path('favorite/', FavoriteListView.as_view(), name='favoritelist'),
     path('remove-product/<uuid:uuid>/', RemoveProductInFavoriteView.as_view(), name='removeproduct'),
     path('add-to-shopcart/<uuid:uuid>/', AddToShopCartView.as_view(), name='addtoshopcart'),
]