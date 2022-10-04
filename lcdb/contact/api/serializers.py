from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ViewSet
from ..models import User
from django.conf import settings


class UserContactSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email",
                  "name",
                  "surname",
                  "phone_number",
                  "comment"]
