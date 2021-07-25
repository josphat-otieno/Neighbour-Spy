from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login
 
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    businesses = Business.objects.all()
    neighbors = Neighbor.objects.all()


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

def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user_form=EditProfileForm(request.POST, request.FILES,instance =request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, f'Your profile was updated successfuly')
            return redirect('profile')
    else:
        user_form=EditProfileForm(instance =request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

        context = {"user_form":user_form, "profile_form":profile_form, "user":user}
        return render(request, 'spys/edit_profile.html', context)


def search(request):
    
    if 'businesses' in request.GET and request.GET["businesses"]:
        search_term = request.GET.get("businesses")
        searched_businesses = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'spy/search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any business"
        return render(request, 'spy/search.html',{"message":message})

