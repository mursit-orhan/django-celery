from rest_framework import generics
from .models import Order, Meal
from rest_framework.response import Response
from .serializers import OrderCreateSerializer, OrderListSerializer, OrderDetailSerializer


def meal_detail(request, pk):
    list_breakfast = Meal.objects.filter(category__exact="BRE")
    context = {'breakfast_list': list_breakfast}


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_read_serializer_class(self):
        if self.request.method == 'POST':
            return OrderDetailSerializer

        return OrderListSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = OrderCreateSerializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = self.perform_create(write_serializer)

        read_serializer = OrderListSerializer(instance)

        return Response(read_serializer.data)


