from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "first_name", "last_name", "username", "password", "email", "address", "city", "state", "zipcode", "phone", "created_date"]


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ["id", "name", "car_color", "car_make", "car_model"]


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ["id", "category", "name", "desc", "price", "qty"]        


class Order_DetailsSerializer(serializers.ModelSerializer):
    # food_name = serializers.ReadOnlyField(source="name") # Research what this does
    food_name = serializers.ReadOnlyField(source = "food_id.name")

    # def get_food_name(self, obj):
    #      return obj.food_id.name if obj.food_id else None

    class Meta:
        model = Order_Details
        fields = ["id", "food_id", "food_name", "order_id", "qty", "tag", "spiciness", "special_instructions"]


class OrderSerializer(serializers.ModelSerializer):
    # customer_name = serializers.SerializerMethodField()
    customer_name = serializers.ReadOnlyField(source="name.first_name")
    driver_name = serializers.ReadOnlyField(source='driver_id.name')
    # driver_name = serializers.SerializerMethodField()
    food_items = Order_DetailsSerializer(many=True, read_only=True)

    # def get_customer_name(self, obj):
    #     return f"{obj.name.first_name} {obj.name.last_name}"
    
    # def get_driver_name(self, obj):
    #     return obj.driver_id.name if obj.driver_id else None 
    
    class Meta:
        model = Order
        fields = ["id", 'name', 'driver_id', "customer_name", "status", "delivery", "special_instructions", "time_placed", "driver_name", "food_items"]


class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()

    def get_customer_name(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name}"
    
    class Meta:
        model = Review
        fields = ["id", "customer_name", "created_date", "content", "likes", "shares"]