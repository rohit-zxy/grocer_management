from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from product.api.serializers import ProductSerializer
from product.models import Product


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
