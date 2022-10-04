from rest_framework.views import APIView
from django.core.checks import messages
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, DestroyAPIView, CreateAPIView, \
    UpdateAPIView
from rest_framework.utils.urls import replace_query_param, remove_query_param
from .serializers import UserContactSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, \
    HTTP_500_INTERNAL_SERVER_ERROR, HTTP_204_NO_CONTENT
from django.http import HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.http.response import HttpResponse
from ..models import User
import json
from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
import stripe
import pprint
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from django.db.models.query import QuerySet
from django.db.models import Q
from pathlib import Path
import time
import pprint
import threading
import multiprocessing
import datetime
import os


class UserContactView(APIView):
    serializer_class = UserContactSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        print(request.data)

        return Response({"message": "OK"}, status=HTTP_200_OK)
