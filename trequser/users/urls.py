from django.urls import include, path
from rest_framework import routers
from trequser.users import views


urlpatterns = [
    path('login', views.JWTView.as_view()),
    path('profile', views.ProfileView.as_view())
]