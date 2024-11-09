from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Category, Brands, CarVilla, Testimonals, About



def IndexView(request):
     brands = Brands.objects.filter(is_active=True).all()
     testimonal = Testimonals.objects.filter(is_active=True).order_by('?')
     cars = CarVilla.objects.filter(is_active=True).all()
     featured_cars = CarVilla.objects.filter(is_featured=True)[:4]
     latest_cars = CarVilla.objects.filter(is_published=True)[:4]


     context = {
          'brands': brands,
          'testimonal': testimonal,
          'cars': cars,
          'featured_cars': featured_cars,
          'latest_cars': latest_cars,
     }
     return render(request, 'index.html', context)




def category_list(request):
     ctg_list = Category.objects.filter(is_active=True)

     context = {
          'ctg_list': ctg_list,
     }
     return render(request, 'base.html', context)




def brandView(request, uuid):
     brand = get_object_or_404(Brands, id=uuid)
     brand_cars = brand.brand_car.all()


     context = {
          'brand': brand,
          'brand_cars': brand_cars,
     }
     return render(request, 'brand_cars.html', context)



def categoryView(request, uuid, slug):
     category = get_object_or_404(Category, id=uuid)
     category_cars = category.category_car.all()

     context = {
          'category': category,
          'category_cars': category_cars,
     }

     return render(request, 'category_cars.html', context)




def detailView(request, uuid):
     detail_product = get_object_or_404(CarVilla, id=uuid)

     context = {
          'detail_product': detail_product,
     }
     
     return render(request, 'detail_product.html', context)