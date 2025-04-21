from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Category, Brands, CarVilla, ProductView, Testimonals, About, ContactUs



def IndexView(request):
     category = Category.objects.filter(is_active=True)
     brands = Brands.objects.filter(is_active=True).all()
     testimonal = Testimonals.objects.filter(is_active=True).order_by('?')
     cars = CarVilla.objects.filter(is_active=True).all()
     featured_cars = CarVilla.objects.filter(is_featured=True)[:4]
     latest_cars = CarVilla.objects.filter(is_published=True)[:4]
     most_sell = CarVilla.objects.filter(is_most_selling=True)


     context = {
          'category': category,
          'brands': brands,
          'testimonal': testimonal,
          'cars': cars,
          'featured_cars': featured_cars,
          'latest_cars': latest_cars,
          'most_sell': most_sell,
     }
     return render(request, 'products/index.html', context)




def brandView(request, uuid):
     brand_view = get_object_or_404(Brands, id=uuid)
     brand_cars = brand_view.brand_car.all()


     context = {
          'brand_view': brand_view,
          'brand_cars': brand_cars,
     }
     return render(request, 'products/brand_cars.html', context)



def categorydetailView(request, uuid):
     category = get_object_or_404(Category, id=uuid)
     category_cars = category.category_car.all()

     context = {
          'category': category,
          'category_cars': category_cars,
     }

     return render(request, 'products/ctg_detail_list.html', context)



def detailView(request, uuid):
     detail_product = get_object_or_404(CarVilla, id=uuid)
     related_product = CarVilla.objects.filter(is_featured=True).order_by('?')[:4]
     if request.user.is_authenticated:
          view, created = ProductView.objects.get_or_create(user=request.user, product=detail_product)

          if created:
               detail_product.views += 1
               detail_product.save()


     context = {
          'detail_product': detail_product,
          'related_product': related_product,
     }
     
     return render(request, 'products/detail_product.html', context)




class ContactView(View):
     def get(self, request):
          return render(request, 'products/contact_page.html')


     def post(self, request):
          contact = ContactUs()
          data = request.POST

          contact.full_name = data.get('full_name')
          contact.email = data.get('email')
          contact.telephone = data.get('telephone')
          contact.message = data.get('message')

          contact.save()

          messages.success(request, "So'rovingiz yuborildi")
          return redirect('contactview')



class SearchView(View):
     def get(self, request):
          query = request.GET.get('search')
          print(query)
          if not query:
               return redirect('indexview')

          search_result = CarVilla.objects.all().filter(Q(model__icontains = query) | Q(description__icontains = query))
          if not search_result:
               messages.warning(request, "So'rov bo'yicha ma'lumot topilmadi")
               return redirect('indexview')

          context = {
               'searchnews': search_result 
          }
          messages.info(request, 'Siz izlagan xabarlar')
          return render(request, 'products/search.html', context)