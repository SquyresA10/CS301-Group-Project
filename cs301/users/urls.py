from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name="landingPage"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
