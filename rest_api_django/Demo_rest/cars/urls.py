from django.urls import path
from .views import *

app_name = 'cars'

urlpatterns = [
    path('create_car/', CarCreationView.as_view()),
    path('list_car/', CarListView.as_view()),
    path('update_car/<int:pk>/', CarDetailView.as_view()),


]
