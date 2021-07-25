from django import forms
from django.contrib.auth.models import User
from .models import Profile, Neighbor, Business
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.contrib.auth.forms import UserChangeForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class': 'form-control'}))
    
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'phone_number', 'bio',]
