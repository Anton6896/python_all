from django.urls import path
from .views import *

app_name = 'cars'

urlpatterns = [
    path('create_car/', CarCreationView.as_view()),
    
]
