from django import forms
from .models import Payment
import re



class ShopAddressForm(forms.ModelForm):
     class Meta:
          model = Payment
          fields = ['country', 'address', 'phone']
          widgets = {
               'country': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Viloyat yoki Shahar kiriting',
                    'required': 'required'
               }),
               'address': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Manzil',
                    'required': 'required'
               }),
               'phone': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': '+998 99 999 99 99',
                    'required': 'required'
               }),
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
                    'max_length': 'Manzil 255 ta belgidan oshmasligi kerak!',
               },
               'phone': {
                    'required': 'Telefon raqamni kiriting!',
                    'max_length': 'Telefon raqam 13 ta belgidan oshmasligi kerak!',
               },
          }

     def clean_phone(self):
          phone = self.cleaned_data.get('phone')
          pattern = r'^\+998\d{9}$'
          if not re.match(pattern, phone):
               raise forms.ValidationError("Telefon raqam +998 bilan boshlanishi va jami 13 ta belgi bo‘lishi kerak!")
          return phone
