from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from django.contrib import messages

# Create your views here.
# def sign_out(request):
#     logout(request)
#     redirect('home')
from django.contrib.auth import logout
from django.shortcuts import redirect

def sign_out(request):
    logout(request)
    # Optionally, you can redirect the user to a specific page after logout.
    return redirect('home')
    


def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            email=request.POST.get('email')
            phone=request.POST.get('phone')
#create user accts
            user=User.objects.create_user(
            username=username,
            password=password,
            email=email
            )    
            customer=Customer.objects.create(
            name=username,    
            user=user,
            phone=phone
            )
            success_message="User Registered Successfully!!!!"
            messages.success(request,success_message)
        
        except Exception as e:
            error_message="Duplicate Username or Invalid Inputs"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')  
        print(username,password)
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('home') 
        else:
            messages.error(request,"Invalid Credentials")

     
    return render(request,"account.html",context)
