from django.urls import path
from .views import HomeView, SignUpView, AccountView

app_name = 'pages'
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('account_detais/',AccountView.as_view(), name='account')
]