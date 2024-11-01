from django.shortcuts import render
from django.views import View
from .models import Category, Brands, CarVilla, Testimonals, About



def IndexView(request):
     brands = Brands.objects.filter(is_active=True).all()
     testimonal = Testimonals.objects.filter(is_active=True).order_by('?')
     cars = CarVilla.objects.filter(is_active=True).all()

     context = {
          'brands': brands,
          'testimonal': testimonal,
          'cars': cars,
     }
     return render(request, 'index.html', context)




def category_list(request):
     ctg_list = Category.objects.filter(is_active=True)

     context = {
          'ctg_list': ctg_list,
     }
     return render(request, 'base.html', context)




# def testimonals(request):
#      testimonal = Testimonals.objects.all()[:3]


#      context = {
#           'testimonal': testimonal,
#      }
#      return render(request, 'index.html', context)
