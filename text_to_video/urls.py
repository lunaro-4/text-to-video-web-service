from django.urls import path, include
from .views import *

urlpatterns = [
    path('main', main_view, name='main'),
    
]
