# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Notification, DayUserAssociation, Market

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Notification
        fields = '__all__'

class DayUserAssociationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = DayUserAssociation
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    marketuser = serializers.PrimaryKeyRelatedField(queryset=DayUserAssociation.objects.all())

    class Meta:
        model = Market
        fields = '__all__'
