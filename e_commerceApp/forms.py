from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *



class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username','email','password1','password2','user_type']

class AuthForm(AuthenticationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username','password1']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerProfileModel
        fields = '__all__'
        exclude = ['user']

class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminProfileModel
        fields = '__all__'
        exclude = ['user']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        exclude = ['user']
        
class ProductManagementForm(forms.ModelForm):
    class Meta:
        model = ProductManagementModel
        fields = '__all__'
        exclude = ['user']
        
class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrderModel
        fields = '__all__'
        exclude = ['product','customer','payment_status','order_status']
        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = '__all__'
        exclude = ['product','customer']
        
