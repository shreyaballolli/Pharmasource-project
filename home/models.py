from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from .models import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class donor1(models.Model):
   Tabletname=models.CharField(max_length=20)
   
   Quantity= models.IntegerField(max_length=50)
   desc= models.TextField()
   Expiry=models.DateField() 
         

class  reciever1(models.Model):  
   tablet=models.CharField(max_length=20)
   Required_Qty= models.IntegerField(max_length=50)
   Prescribed_by= models.CharField(max_length=20)
  

class CreateUserForm(UserCreationForm):
   class Meta:
         model=User
         fields=['username','email','password1','password2']
# class signup1(models.Model) :
#    Username=models.CharField(max_length=20)
#    email=models.CharField(max_length=30)
#    psw=models.CharField(max_length=20)
#    psw_repeat=models.CharField(max_length=20)

# class login1(models.Model) :
#    Username=models.CharField(max_length=20)
#    Psw=models.CharField(max_length=20)
   