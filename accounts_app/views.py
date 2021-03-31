from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messege = "Invalid username or password"
            return render(request,"login.html",{"messege":messege})

    return render(request,'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

    
