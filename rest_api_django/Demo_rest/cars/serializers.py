from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    # on crete connect tu user
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'vin', 'user', 'color')
