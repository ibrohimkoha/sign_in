from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from accounts.forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request,'index.html')

    def post(self, request):
        return render(request,'index.html')

def logout_user(request):
    logout(request)
    messages.success("chiqdingiz")
    return render(request,'index.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name ='registration/signup.html'

class AccountView(View):
    def get(self, request):
        return render(request,'account.html')

    def post(self, request):
        return render(request,'account.html')

