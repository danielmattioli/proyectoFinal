from django import forms

class cuentaForm(forms.Form):
    user = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    password = forms.PasswordInput()