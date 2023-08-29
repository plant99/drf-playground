from django.urls import include, path
from rest_framework import routers
from trequser.users import views

user_list = views.UserViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('login', views.JWTView.as_view()),
    path('profile', views.ProfileView.as_view()),
    path('list', user_list)
]