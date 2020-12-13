from rest_framework import generics
from .serializers import CarDetailSerializer

class CarCreationView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


