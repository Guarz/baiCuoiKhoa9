from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# creating a form
class InputForm(forms.Form):
    msgv = forms.CharField(max_length = 200)
    name = forms.CharField(max_length = 200)
    email = forms.CharField(max_length = 200)
    phone = forms.CharField(max_length = 200)
    date = forms.CharField(max_length = 200)
    gender = forms.CharField(max_length = 200)
# class Login(forms.Form):
#     username = forms.CharField(max_length = 200)
#     password = forms.CharField(max_length = 200)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('sex_choice',)
        fields = UserCreationForm.Meta.fields + ('age',)
        fields = UserCreationForm.Meta.fields + ('sex',)
        fields = UserCreationForm.Meta.fields + ('address',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields