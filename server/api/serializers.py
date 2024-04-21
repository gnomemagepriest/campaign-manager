from re import I
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: list[str] = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        user: User = User.objects.create_user(**validated_data)
        return user

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields: list[str] = ["id", "title", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields: list[str] = ["id", "name", "type", "description", "campaign"]
        extra_kwargs = {"campaign": {"read_only": True}}

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields: list[str] = ["id", "name", "description", "campaign"]
        extra_kwargs = {"campaign": {"read_only": True}}

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields: list[str] = ["id", "name", "description", "campaign"]
        extra_kwargs = {"campaign": {"read_only": True}}

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields: list[str] = ["id", "name", "description", "campaign"]
        extra_kwargs = {"campaign": {"read_only": True}}
