from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
# Create your views here.

# sign up code
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"psw not match")
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'reg_app/register.html')


# login code
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'reg_app/login.html')

# logout code
def logout(request):
    auth_logout(request)
    return  redirect('/')