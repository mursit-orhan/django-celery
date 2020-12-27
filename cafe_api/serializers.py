from rest_framework import serializers
from .models import Order, Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'table_number', 'meals')

    def create(self, validated_data):
        meals = validated_data.pop('meals')
        instance = Order.objects.create(**validated_data)
        for meal in meals:
            instance.meals.add(meal)

        return instance


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
