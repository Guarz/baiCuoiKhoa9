from django import forms

# creating a form
class InputForm(forms.Form):
    msgv = forms.CharField(max_length = 200)
    name = forms.CharField(max_length = 200)
    email = forms.CharField(max_length = 200)
    phone = forms.CharField(max_length = 200)
    date = forms.CharField(max_length = 200)
    gender = forms.CharField(max_length = 200)
    