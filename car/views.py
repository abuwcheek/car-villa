from django.shortcuts import render
from .models import Category, Brands, CarVilla, Testimonals, About



def IndexView(request):
     return render(request, 'index.html')




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

