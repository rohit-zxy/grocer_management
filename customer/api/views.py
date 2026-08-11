from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from customer.models import Customer
from customer.api.serializers import CustomerSerializer


class CustomerListAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
