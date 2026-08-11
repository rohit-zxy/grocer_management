from django.urls import path
from Orders.api.views import OrderListAPIView, OrderDetailAPIView

urlpatterns = [
    path('create/', OrderListAPIView.as_view(), name='order-list'),
    path('edit-delete-get-order/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail')
]

