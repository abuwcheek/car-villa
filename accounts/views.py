from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserLoginForm
from django.views import View
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login, logout


class UserRegisterView(View):
    form = UserRegisterForm

    def get(self, request):
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
            return redirect('home:all')

        messages.warning(request, "Ro'yxatdan o'ta olmadingiz")
        context = {
            'form': user_form,
        }
        return render(request, 'accounts/register.html', context)


class UserLoginView(View):
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        contex = {
            'form': form,
        }

        return render(request, 'accounts/login.html', contex)


    def post(self, request):
        user_form = self.form_class(data=request.POST)

        if user_form.is_valid():
            user = authenticate(request, username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.success(request, "Tizimga muvaffaqiyatli kirdingiz.")
                return redirect('home')

            messages.warning(request, "Username yoki parol noto'g'ri")
            contex = {
                'form': user_form,
            }

            return render(request, 'accounts/login.html', contex)

        messages.error(request, user_form.errors)
        contex = {
            'form': user_form,
        }

        return render(request, 'accounts/login.html', contex)