from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login
 
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'spy/index.html')

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
        return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'django_registration/registration_form.html', {"form":form})

def profile_view(request):
    user = request.user
    user = User.objects.get(username = user.username)
    return render (request, 'spy/profile.html', {"user":user})
