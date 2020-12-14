from rest_framework import generics, permissions
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly


class CarCreationView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class CarByColor(generics.ListAPIView):
    serializer_class = CarListSerializer

    # http://127.0.0.1:8001/api/v1/cars/color_car/?q=green
    # http://127.0.0.1:8000/api/v1/cars/list_car/
    def get_queryset(self):
        if self.request.method == 'GET':

            q = self.request.GET.get('q', None)
            if q is not None:
                queryset = Car.objects.filter(color=q).all()
            return queryset


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer  # build in class
    queryset = Car.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
