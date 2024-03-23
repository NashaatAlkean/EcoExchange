from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

#cteate class for user regester form that inherate from UserCreationForm
class RegisterUserForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['email','password1','password2']



class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', max_length=100)
    mobile = forms.CharField(label='Mobile', max_length=20)
    address = forms.CharField(label='Address')
    bio=forms.CharField(label="bio",widget=forms.Textarea)
    image=forms.ImageField(label="Profile picture")
    class Meta:
        model=Profile
        fields=['full_name','mobile','address','bio','image']

