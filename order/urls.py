from django.urls import path
from .views import AddToFavoriteView, FavoriteListView, remove_wishlist_product, AddToShopCartView, ShopCartProductView, delete_shop_cart, clear_cart, ShopAddressView, PaymentView



app_name = 'order'
urlpatterns = [
     path('order-to-favorite/', AddToFavoriteView.as_view(), name='addtofavorite'),
     path('favorite/', FavoriteListView.as_view(), name='favoritelist'),
     path('remove-product/<uuid:uuid>/', remove_wishlist_product, name='removeproduct'),
     path('add-to-shopcart/<uuid:uuid>/', AddToShopCartView.as_view(), name='addtoshopcart'),
     path('shop-cart/', ShopCartProductView.as_view(), name='shop-cart',),
     path('delete-shop-cart/<uuid:uuid>/', delete_shop_cart, name='delete-shop-cart'),
     path('clear-cart/', clear_cart, name='clear-cart'),
     path('shop-address/', ShopAddressView.as_view(), name='shop-address'),
     path('payment/<uuid:uuid>/', PaymentView.as_view(), name='payment')
] 