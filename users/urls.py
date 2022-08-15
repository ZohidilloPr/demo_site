from django.urls import path
from .views import LOGIN, LOGOUT

app_name = 'users'

urlpatterns = [
    path("", LOGIN, name="LG"),
    path("logout/", LOGOUT, name="LO"),
]