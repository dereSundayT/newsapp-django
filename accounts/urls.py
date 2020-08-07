from django.urls import path
from .views import register, Login, Logout

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Login.as_view(), name="logout"),
]
