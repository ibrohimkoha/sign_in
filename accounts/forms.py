from django.forms import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name','email','image')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('first_name','last_name','image')

