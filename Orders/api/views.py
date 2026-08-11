from .serializers import OrderSerializer
from Orders.models import Order

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class OrderListAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
