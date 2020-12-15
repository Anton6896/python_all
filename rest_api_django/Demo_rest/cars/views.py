from rest_framework import generics, permissions
from .serializers import CarDetailSerializer, CarListSerializer
from .models import Car
from .permissions import IsOwnerOrReadOnly

# ############  crud section 

class CarCreationView(generics.CreateAPIView):
    # http://127.0.0.1:8000/api/v1/cars/create_car
    serializer_class = CarDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CarListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/v1/cars/list_car/
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CarByColor(generics.ListAPIView):
    # http://127.0.0.1:8000/api/v1/cars/color_car/?q=green
    serializer_class = CarListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            q = self.request.GET.get('q', None)  # get color ?q=green
            if q is not None:
                return Car.objects.filter(color=q).all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/v1/cars/update_car/1
    serializer_class = CarDetailSerializer  # build in class
    queryset = Car.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

 
# ############ user section 