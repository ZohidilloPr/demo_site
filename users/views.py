from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def LOGIN(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("H")
    form = AuthenticationForm
    return render(request, "users/login/login.html", {
        "form":form
    })

def LOGOUT(request):
    logout(request)
    return redirect("users:LG")