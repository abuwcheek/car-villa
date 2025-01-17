from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from .forms import CastumAuthForm, UserRegisterForm
from django.contrib import messages
from PIL import Image
from django.db.models import Q
from .models import User




class UserRegisterView(View):
     form = UserRegisterForm

     def get(self,  request):
          if not request.user.is_authenticated:
               context = {
                    'form': self.form
               }
               return render(request, 'accounts/register.html', context)
          messages.warning(request, 'Siz avval tizimdan chiqishingiz kerak')
          return redirect('index')


     def post(self, request):
          user_form = self.form(data=request.POST, files=request.FILES)
          if user_form.is_valid():
               user_form.save()
               messages.success(request, "Ro'yxatdan o'tdingiz")
               return redirect('index')

          messages.warning(request, "Ro'yxatdan o'ta olmadingiz")
          context={
               'form':user_form,
               }
          return render(request, 'accounts/register.html', context)




class LoginView(View):
     def get(self, request):
          if request.user.is_authenticated:
               messages.warning(request, 'Siz tizimdan chiqishingiz kerak')
               return redirect('index')

          form = CastumAuthForm
          context = {
               'form': form,
          }
          return render(request, 'accounts/login.html', context)


     def post(self, request):
          data = request.POST
          form = CastumAuthForm(data=data)
          if form.is_valid():
               user = form.get_user()
               login(request, user)
               messages.success(request, 'Tizimga kirdingiz')
               return redirect('index')
          else:
               messages.warning(request, 'Parol yoki login xato')
               return render(request, 'accounts/login.html', {'form':form})


class UserProfileView(View):
     def get(self, request):
          if request.user.is_authenticated:
               user = User.objects.get(id=request.user.id)

               context = {
                    'user': user,
               }
               return render(request, 'accounts/myprofile.html', context)
          messages.warning(request, 'Siz oldin tizimga kirishingiz kerak!')
          return redirect('accounts:login')