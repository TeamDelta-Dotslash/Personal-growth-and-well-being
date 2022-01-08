from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import audio_forms
from .models import audio
# Create your views here.
def index(request):
    all_audio = audio.objects.all()
    if request.method == "POSt":
        form = audio_forms(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded Successfully </h1>")
        else:
            form = audio_forms()
        return render(request,'index.html',{"form":form,"all":all_audio})
    return render(request, 'index.html')

def registration(request):
    if request.method == "POST":
        user_form =RegistrationForm(request.POST)
        if user_form.is_valid:
            user_form.save()
            return HttpResponse("<h1> User Registered Successfully</h1>")
    else:
        user_form = RegistrationForm()
    return render(request, 'registration.html', {'user_form':user_form})

    ######## Login Form
    
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            user = authenticate(request, username=cd["username"], password = cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("<h1> Login successfully </h1>")
                else:
                    return HttpResponse("<h1> User Deactivated </h1>")
            else:
                return HttpResponse("<h1> Invalid Login </h1>")
    else:
        form=LoginForm()
    return render(request, "login.html", {"form": form})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponse("<h1> LogOut Successfully</h1>")
