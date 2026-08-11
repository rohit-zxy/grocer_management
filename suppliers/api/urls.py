from django.urls import path

from suppliers.api.views import SupplierDetailAPIView, SupplierListAPIView


urlpatterns = [
    path("create/", SupplierListAPIView.as_view(), name="supplier-list"),
    path("edit-delete-get-supplier/<int:pk>/", SupplierDetailAPIView.as_view(), name="supplier-detail"),
]
