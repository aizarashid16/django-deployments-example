from django.urls import path
from authenapp import views

app_name="authenapp"
urlpatterns=[
    path("register/",views.register,name="register"),
    path("user_login/",views.user_login,name="user_login"),
]
