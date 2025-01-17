from django import forms
from django.forms.widgets import TextInput, PasswordInput, EmailInput
from .models import User

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={}), required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={}), required=True)

    password = forms.CharField(widget=forms.PasswordInput(attrs={}), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={}), required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email oldin ro'yxatdan o'tgan")

        return email



    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu username oldin ro'yxatdan o'tgan")

        return username



    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 != password2:
            raise forms.ValidationError("Parollar bir biriga mos emas!")

        return password2


    def save(self, commit=True):
        password = self.cleaned_data.get('password')

        user = super().save(commit)
        user.set_password(password)
        user.save()

        return user



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={}), required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not username or not password:
            raise forms.ValidationError("Maydonlar bo'sh bo'lmasligi lozim")

        return self.cleaned_data