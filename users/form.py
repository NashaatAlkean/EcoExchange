from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

#cteate class for user regester form that inherate from UserCreationForm
class RegisterUserForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=['email','password1','password2']
        