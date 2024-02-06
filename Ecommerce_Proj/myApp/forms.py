from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Customer

class RegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'mobile', 'pincode', 'state', 'city']

class CustomPassResetForm(PasswordResetForm):
    class Meta:
        fields = ['email']

class CustomPassChangeForm(PasswordChangeForm):
     class Meta:
        fields = ['old_password']

class CustomeSetNewPassword(SetPasswordForm):
    pass
             
     
  
     
    
    