from django.contrib.auth.urls import path
from attend import views

urlpatterns = [
    path('user', views.userpage, name='user'),
    path('', views.adminpage, name='superuser'),
    path('register', views.registration, name='register'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('add_user', views.adduser, name='add_user'),
    path('attend', views.userattendence, name='attend'),
    path('all_attend', views.alluserattendence, name='all_attend'),

]
