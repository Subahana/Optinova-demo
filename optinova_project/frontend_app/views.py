from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signin_view(request):
    return render(request,'signin_signup/signin_view.html')

def signup_view(request): 
    form=UserCreationForm()

    if request.method == 'POST' :
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('signin_view')

def landing_page(request):
    return render(request,'frontend/index.html')

