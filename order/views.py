from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Sevimlilar
from car.models import CarVilla


class AddToSevimlilarView(View):
     def get(self, request):
          user = request.user
          url = request.META.get('HTTP_REFERER')
          product = request.GET.get('product_id')
          product = CarVilla.objects.get(id=product)
          Sevimlilar.objects.create(user=user, product=product)
          messages.success(request, 'Mahsulot sevimlilarga qo\'shildi')
          return redirect(url)



class FavoriteView(View):
     def get(self, request):
          user = request.user
          if not user.is_authenticated:
               messages.warning(request, "Siz oldin Login qilishingiz kerak")
               return redirect('users:login')

          sevimlilar = Sevimlilar.objects.filter(user=user)
          context = {
               'sevimlilar': sevimlilar,
          } 
          return render(request, 'products/shop-wishlist.html', context)


