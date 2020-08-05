from django.urls import path
from .views import register, Login

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', Login.as_view(), name="login"),
]
