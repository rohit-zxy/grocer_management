from django.urls import path

from product.api.views import ProductDetailAPIView, ProductListAPIView


urlpatterns = [
    path("create/", ProductListAPIView.as_view(), name="product-list"),
    path("edit-delete-get-product/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
]
