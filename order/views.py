from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from .models import Sevimlilar, AddToShopCart
from car.models import CarVilla

class AddToFavoriteView(View):
    def get(self, request):
        user = request.user
        url = request.META.get('HTTP_REFERER')
        product_id = request.GET.get('product_id')

        if not product_id:
            messages.error(request, "Mahsulot ID si topilmadi!")
            return redirect(url)

        product = get_object_or_404(CarVilla, id=product_id)

        # ✅ Wishlistda bor yoki yo‘qligini tekshirish
        favorite, created = Sevimlilar.objects.get_or_create(user=user, product=product)

        if not created:
            messages.warning(request, "Bu mahsulot allaqachon sevimlilarda bor!")
        else:
            messages.success(request, "Mahsulot sevimlilarga qo‘shildi!")

        return redirect(url)



class FavoriteListView(View):
    def get(self, request):
        user = request.user
        sevimlilist = Sevimlilar.objects.filter(user=user)
        context = {
            'sevimlilist': sevimlilist,
        }
        return render(request, 'order/shop-wishlist.html', context)



def remove_wishlist_product(request, uuid):
    sevimli_remove = get_object_or_404(Sevimlilar, id=uuid)
    sevimli_remove.delete()
    messages.info(request, "Mahsulot sevimlilardan o'chirildi!")
    return redirect('order:favoritelist')



class AddToShopCartView(View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')  # Qayerdan kelinganini olish
        user = request.user
        product = get_object_or_404(CarVilla, id=uuid)  # Mahsulotni olish
        
        # 🔥 Mahsulot allaqachon qo‘shilganmi, tekshiramiz
        if AddToShopCart.objects.filter(user=user, product=product).exists():
            messages.warning(request, "Bu mahsulot allaqachon savatchaga qo'shilgan!")
        else:
            AddToShopCart.objects.create(user=user, product=product)
            messages.success(request, "Mahsulot savatchaga qo'shildi!")

        return redirect(url)