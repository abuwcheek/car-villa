from django import forms
from .models import Payment




class ShopAddressForm(forms.ModelForm):
     class Meta:
          model = Payment
          fields = ['country', 'address', 'phone']
          widgets = {
               'country': forms.TextInput(attrs={'class': 'form.control'}),
               'address': forms.TextInput(attrs={'class': 'form.control'}),
               'phone': forms.TextInput(attrs={'class': 'form.control'}),
          }