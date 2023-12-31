from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm , UserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserChangeForm
    form = UserCreationForm
    model = CustomUser
    list_display = ('username', 'email')
admin.site.register(CustomUser, CustomUserAdmin)