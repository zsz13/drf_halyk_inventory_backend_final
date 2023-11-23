from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import InventoryItem
from .permissions import IsAdmin
from .serializers import InventoryItemSerializer


class InventoryItemAPIList(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = (IsAuthenticated, )


class InventoryItemAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = (IsAdmin,)


class InventoryItemAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = (IsAdmin,)

