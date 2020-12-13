from rest_framework import generics
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car


class CarCreationView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer  # build in class 
    queryset = Car.objects.all() 

