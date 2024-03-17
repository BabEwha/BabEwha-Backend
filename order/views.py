from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from .models import Order
from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # User 정보 추가

    @action(detail=False, methods=['get'], url_path='(?P<group_id>[^/.]+)/details')
    def group_order_details(self, request, group_id=None):
        orders = get_list_or_404(Order, group__id=group_id)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['get'], url_path='order-details')
    def order_details(self, request, pk=None):
        group_id = pk
        orders = Order.objects.filter(
            group_id=group_id, 
            order_status='ordered', 
            user__participate__is_active=True,
            user__participate__group_id=group_id
        ).distinct()


