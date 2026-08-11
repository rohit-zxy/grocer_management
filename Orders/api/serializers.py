from rest_framework import serializers
from Orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["order_id", "customer", "order_date", "status", "order_details"]
