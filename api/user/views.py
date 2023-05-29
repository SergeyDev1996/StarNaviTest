from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from api.user.serializers import UserSignUpSerializer


class UserSignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer
