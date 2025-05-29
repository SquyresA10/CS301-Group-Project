from django.urls import path
from . import views

urlpatterns = [
    #path('', views.landing, name="index"),
    path('', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path('index/', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
