from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import UserContactView

urlpatterns = [
    path('contact_list/', UserContactView.as_view(), name="user_contact_view"),
    ]
