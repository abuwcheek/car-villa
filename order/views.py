from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Sevimlilar, AddToShopCart, Payment
from .forms import ShopAddressForm
from car.models import CarVilla



class AddToFavoriteView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
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
        else:
            messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
            return redirect('users:login')

        return redirect(url)



class FavoriteListView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            sevimlilist = Sevimlilar.objects.filter(user=user)
            context = {
                'sevimlilist': sevimlilist,
            }
            return render(request, 'order/shop-wishlist.html', context)
        else:
            messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
            return redirect('users:login')

def remove_wishlist_product(request, uuid):
    sevimli_remove = get_object_or_404(Sevimlilar, id=uuid)
    sevimli_remove.delete()
    messages.info(request, "Mahsulot sevimlilardan o‘chirildi!")
    return redirect('order:favoritelist')



class AddToShopCartView(View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')  # Qayerdan kelinganini olish
        user = request.user
        if user.is_authenticated:
            product = get_object_or_404(CarVilla, id=uuid)  # Mahsulotni olish
            
            # 🔥 Mahsulot allaqachon qo‘shilganmi, tekshiramiz
            if AddToShopCart.objects.filter(user=user, product=product).exists():
                messages.warning(request, "Bu mahsulot allaqachon savatchaga qo‘shilgan!")
            else:
                cart_item = AddToShopCart.objects.create(user=user, product=product)
                cart_item.save()
                messages.success(request, "Mahsulot savatchaga qo‘shildi!")

            return redirect(url)
        else:
            messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
            return redirect('users:login')



class ShopCartProductView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            user = request.user
            orders = AddToShopCart.objects.filter(Q(user=user))

            total = 0
            for item in orders:
                total += item.product.get_new_price * item.quantity

            context = {
                'orders': orders,
                'total': total,
            }
            return render(request, 'order/shop-cart.html', context)
        else:
            messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
            return redirect('users:login')



def delete_shop_cart(request, uuid):
    order = AddToShopCart.objects.get(id=uuid)
    order.delete()
    messages.info(request, "Mahsulot o‘chirildi")
    return redirect('order:shop-cart')



def clear_cart(request):
    user = request.user
    if user.is_authenticated:
        orders = AddToShopCart.objects.filter(Q(user=user) & Q(status="to'lanmagan"))
        if not orders:
            messages.warning(request, "Savatcha bo'sh")
            return redirect('order:shop-cart')
        
        for order in orders:
            order.delete()
        messages.info(request, "Savatcha tozalandi")
        return redirect('order:shop-cart')
    else:
        messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
        return redirect('users:login')



class ShopAddressView(View):
    def get(self, request):
        user=request.user
        if user.is_authenticated:
            form = ShopAddressForm()
            context = {
                'form': form
            }
            return render(request, 'order/shop-address.html', context)
        else:
            messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
            return redirect('users:login')



    def post(self, request):
        user = request.user
        if user.is_authenticated:
            orders = AddToShopCart.objects.filter(Q(user=user) & Q(status="to'lanmagan"))
        
            form = ShopAddressForm(request.POST)
            if form.is_valid():
                payment = form.save(commit=False)
                for order in orders:
                    payment.order.add(order)
                payment.save()

                return redirect('order:payment', uuid=payment.id)
            else:
                messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
                return redirect('users:login')




class PaymentView(View):
    def get(self, request, uuid):
        user=request.user
        if user.is_authenticated:
            total = 0
            payment = Payment.objects.get(id=uuid)
            for order in payment.order.all().filter(status=False):
                total += order.product.get_new_price * order.quantity

            context = {
                'total': total
            }
            return render(request, 'order/cart-total.html', context)
        else:
            messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
            return redirect('users:login')


    
    def post(self, request, uuid):
        user=request.user
        if user.is_authenticated:
            payment = Payment.objects.get(id=uuid)
            for order in payment.order.all():
                order.status = True
                order.save()

            messages.success(request, "Mahsulotlar yuborildi")
            return redirect('order:favoritelist')
        else:
            messages.warning(request, "Siz oldin tizimga kirishingiz kerak")
            return redirect('users:login')
