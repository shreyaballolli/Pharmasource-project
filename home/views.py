from django.shortcuts import render,redirect
from datetime import datetime
from home.models import donor1
from home.models import reciever1
# from home.models import signup1
# from home.models import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from .filters import donor1Filter
# Create your views here.



def home(request):
    return render(request,'index.html')
# # return HttpResponse("This is home page")

def donor(request):
    if request.method =="POST":
        Tabletname=request.POST.get('Tabletname')
        Quantity=request.POST.get('Quantity')
        desc=request.POST.get('desc')
        Expiry=request.POST.get('Expiry')
        Donor=donor1(Tabletname=Tabletname,Quantity=Quantity,desc=desc,Expiry=Expiry)
        Donor.save()
    return render(request,'donor.html')

def reciever(request):
    if request.method =="POST":
        tablet=request.POST.get('tablet')
        Required_Qty=request.POST.get('Required_Qty')
        Prescribed_by=request.POST.get('Prescribed_by')
        Reciever=reciever1(tablet=tablet,Required_Qty=Required_Qty,Prescribed_by=Prescribed_by)
        Reciever.save()
    return render(request,'reciever.html')


def signup(request):
    form=UserCreationForm()


    if request.method == 'POST':
     form= UserCreationForm(request.POST)
    if form.is_valid():
     form.save()
     user=form.cleaned_data.get('username')
     messages.success(request,'Account was created for'  +user)
     return redirect('login')
    context={'form':form}
    return render(request,'signup.html',context)


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password) 
        if user is not None:
          auth.login(request,user)
          return redirect('home')
        else:
            messages.info(request,'Username OR password is incorrect')
        # context={}
    return render(request,'login.html')


def adminslogin(request):
     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('admin1') 
        else:
             messages.info(request,'Username OR password is incorrect')
        

     return render(request,'adminslogin.html') 

def admin1(request):
    # if request.method=='POST':
    if request.method == "POST":
        # searched = request.POST['searched']
        posts= donor1.objects.all()
        # searched = request.POST.get('searched')
        # posts=donor1.objects.filter(Tabletname__contains=searched)
        context= {'donor1':posts}
        print(posts)
        return render(request , 'admin1.html' ,context ) 

    else:  
      return render(request,'admin1.html',{})   


def search(request):
    if request.method == "POST":
        # searched = request.POST['searched']
        posts= donor1.objects.all()
        # searched = request.POST.get('searched')
        # posts=donor1.objects.filter(Tabletname__contains=searched)

        return render(request , 'search.html' , {'donor1':donor1}) 

    else:  
      return render(request , 'search.html',{}) 

def logoutUser(request):
    logout(request)
    return redirect('login')