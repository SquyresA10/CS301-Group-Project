from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

#Registration view
def register(request):
    if request.method == 'POST':
        username = request.POST['firstname'].title()
        firstname = request.POST['firstname'].title()
        lastname = request.POST['lastname'].title()
        email = request.POST['email'].lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
    #condition 1 passwords must be the same
        if password1 == password2:
              #condition 2 unique email
              if User.objects.filter(email=email).exists():
                  messages.info(request, 'The email address you entered is already used\nplease try again')
                  return redirect('register')
              else: 
                  user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password2)
                  user.save();
                  messages.info(request,'Your Account has been successfully registered\nYou can now login')
                  return redirect('login')
        else: 
              messages.info(request,'The passwords do not match')
              return redirect('register') 
    else: 
       messages.info(request,'You did not enter any details')         
       return render(request,'register.html')


#This is a login view that handles user login.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username'].title()
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("home")
        else: 
            messages.info(request, "Wrong username or password")
            return render(request, "login.html")          
    return render(request, 'login.html')

#This is a logout view that handles user logout.
def logout_view(request):
    logout(request)
    return redirect('landingPage')

#Landing page view
def landingPage(request):
    return render(request, 'landingPage.html')