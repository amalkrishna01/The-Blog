from django.contrib import admin
from django.urls import path, include
from home import views
from .views import landing,detail,Addpost,Editpost,Deletepost,CategoryView,LikeView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView,AddCommentView

from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('landing/', landing.as_view(), name='landing' ),
    path('detail/<int:pk>/', detail.as_view(), name='detail' ),
    path('add_post/',Addpost.as_view(),name = 'addpost'),
    path('detail/edit/<int:pk>/',Editpost.as_view(),name = 'edit'),
    path('detail/<int:pk>/delete/',Deletepost.as_view(),name = 'delete'),
    path('category/<str:cats>/',CategoryView,name = 'category'),
    path('like/<int:pk>',LikeView, name='like_post'),
    #path('edit_profile/', views.profile , name='profile'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(), name = "show_profile"),
    path('<int:pk>/edit_profile/',EditProfilePageView.as_view(), name = "edit_profile"),
    path('create_profile/',CreateProfilePageView.as_view(), name = "create_profile"),
    path('detail/<int:pk>/comment',AddCommentView.as_view(),name = 'comment'),
   
    
       

]
 
