from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response


from .models import InventoryItem
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import InventoryItemSerializer


class InventoryItemAPIList(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class InventoryItemAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class InventoryItemAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = (IsAdminOrReadOnly, )

