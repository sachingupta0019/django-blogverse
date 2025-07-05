from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import UserProfile
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# Create your views here.

# Login

def user_login(request): 
    if request.method == "POST":
        LoginForm = UserLoginForm(request=request, data=request.POST)
        if LoginForm.is_valid():
            uname = LoginForm.cleaned_data["username"]
            upass = LoginForm.cleaned_data["password"]
            user = authenticate(username=uname, password=upass)
            if user is not None:
                messages.success(request, "Login Successfully !!!.")
                login(request, user)
                return HttpResponseRedirect("/")
        else:
            messages.info(request, "Username or Password is incorrect.")
            return render(request, "users/login.html", {'form':LoginForm})
    else:
        LoginForm = UserLoginForm()
    return render(request, "users/login.html", {'form':LoginForm})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged-out Succesfully!!!.")
    else:
        messages.info(request, "You are authorized.")
    return HttpResponseRedirect('/user/login/')

def user_signup(request):
    if request.method == "POST":
        SignupForm = UserRegistrationForm(request.POST, request.FILES)
        if SignupForm.is_valid():
            messages.success(request, "User Registered Successfully!!!.")
            print(SignupForm.cleaned_data)
            user = SignupForm.save(commit=False)
            user.email = SignupForm.cleaned_data['email']
            user.save()

            # Save custom UserProfile fields manually
            phone = SignupForm.cleaned_data.get('phone')
            gender = SignupForm.cleaned_data.get('gender')
            address = SignupForm.cleaned_data.get('address')
            photo = SignupForm.cleaned_data.get('photo')

            UserProfile.objects.create(
                user=user,
                phone=phone,
                gender=gender,
                address=address,
                photo=photo
            )

            messages.success(request, "User Registered Successfully!")
            return HttpResponseRedirect("/user/login/")
        else:
            messages.error(request, "Try again..")
    else:
        SignupForm = UserRegistrationForm()
    return render(request, "users/signup.html", {'SignupForm':SignupForm})

def user_profile(request):
    return render(request, "users/profile.html")