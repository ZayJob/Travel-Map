from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='tm-home'),
    path('register/', register, name='tm-register'),
]
