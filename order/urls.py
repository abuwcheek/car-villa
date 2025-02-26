from django.urls import path
from .views import AddToFavoriteView, FavoriteListView, remove_wishlist_product, AddToShopCartView



app_name = 'order'
urlpatterns = [
     path('order-to-favorite/', AddToFavoriteView.as_view(), name='addtofavorite'),
     path('favorite/', FavoriteListView.as_view(), name='favoritelist'),
     path('remove-product/<uuid:uuid>/', remove_wishlist_product, name='removeproduct'),
     path('add-to-shopcart/<uuid:uuid>/', AddToShopCartView.as_view(), name='addtoshopcart'),
]