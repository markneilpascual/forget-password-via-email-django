from django.contrib.auth import forms as auth_forms
from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import EmailInput, PasswordInput


class PasswordResetForm(auth_forms.PasswordResetForm):
    email  = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))



class PasswordResetConfirmForm(auth_forms.SetPasswordForm):
    new_password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}), label='New password')
    new_password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}), label='Confirm new password')