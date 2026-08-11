from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from suppliers.api.serializers import SupplierSerializer
from suppliers.models import Supplier


class SupplierListAPIView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
