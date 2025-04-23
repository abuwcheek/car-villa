from django import forms
from .models import Payment




class ShopAddressForm(forms.ModelForm):
     class Meta:
          model = Payment
          fields = ['country', 'address', 'phone']
          widgets = {
               'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Viloyat yoki Shahar kiriting'}),
               'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzil'}),
               'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998 99 999 99 99'}),
          }
          labels = {
               'country': 'Tuman',
               'address': 'Manzil',
               'phone': 'Telefon raqam',
          }
          error_messages = {
               'country': {
                    'required': 'Viloyat yoki Shahar kiriting!',
                    'max_length': 'Mamlakat 50 ta belgidan oshmasligi kerak!',
               },
               'address': {
                    'required': 'Manzilni kiriting!',
                    'max_length': 'Manzil 50 ta belgidan oshmasligi kerak!',
               },
               'phone': {
                    'required': 'Telefon raqamni kiriting!',
                    'max_length': 'Telefon raqam 13 ta belgidan oshmasligi kerak!', 
               },
          }
