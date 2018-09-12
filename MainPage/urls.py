from django.urls import path
from . import views
from django.contrib.auth.views import password_change


urlpatterns = [
    path('', views.MainPage, name="MainPage"),
    path('changeform', views.ChangeForm, name="ChangeForm")

]
