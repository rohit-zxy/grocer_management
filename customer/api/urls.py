from django.urls import path

from customer.api.views import CustomerDetailAPIView, CustomerListAPIView


urlpatterns = [
    path("create/", CustomerListAPIView.as_view(), name="customer-list"),
    path("edit-delete-get-customer/<int:pk>/", CustomerDetailAPIView.as_view(), name="customer-detail"),
]
