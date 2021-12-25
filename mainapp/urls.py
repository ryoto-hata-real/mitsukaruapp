from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.Login.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup',views.signup),
    path('contact',views.contact, name='contact'),
    path('profile',views.profile, name='profile'),
    path('term',views.term,name='term'),
    path('privacy', views.privacy,name='privacy'),
    path('contact-done', views.contactDone, name='contact-done'),
]
