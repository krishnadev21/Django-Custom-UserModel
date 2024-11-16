from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('signup/', views.userSignup, name='signup'),
    path('user-profile/', views.userProfile, name='user-profile'),
    path('user-update/', views.userUpdate, name='user-update'),
]
