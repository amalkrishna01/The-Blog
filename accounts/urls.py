from django.contrib import admin
from django.urls import path, include
from accounts import views
#from .views import UserRegisterView

from accounts.views import(
    registration_view,
    account_view,
    
)

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.Logout, name = 'logout'),
    path('edit_cred/', account_view, name='cred'),
   
    
]
