# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import BucketListSerializer
from .models import BucketList
from .permissions import IsOwner

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)
