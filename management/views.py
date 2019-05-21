# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets, permissions, generics
from .serializers import UserInfoSerializer
from .models import UserInfo
from django.http import HttpResponse

from django.shortcuts import render

class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (permissions.IsAuthenticated,)

def detail(request, name, ):
    # userid = request.GET.get("", "")
    email = UserInfo.objects.filter(name=name)
    # name = UserInfo.objects.all()
    return HttpResponse(email)

