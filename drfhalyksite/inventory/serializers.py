from rest_framework import serializers
from .models import InventoryItem


class InventoryItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = InventoryItem
        fields = "__all__"


