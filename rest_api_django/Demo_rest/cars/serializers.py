from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Car


class CarDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')




