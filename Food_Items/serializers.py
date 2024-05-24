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
    food_name = serializers.ReadOnlyField(source = "food_id.name")

    class Meta:
        model = Order_Details
        fields = ["id", "food_id", "food_name", "order_id", "qty", "tag", "spiciness", "special_instructions"]

#########################################################################  
class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source="name.first_name")     # Displays the customer name at the orders end point
    driver_name = serializers.ReadOnlyField(source='driver_id.name')        # Displays the driver   name at the orders end point
    food_items = Order_DetailsSerializer(many=True, read_only=True)         # Serializes (turns Python object into JSON data? Otherwise is would be just an JSON object rather than spelled out) the food items. Essenentially nests it
                                                                                
    class Meta:
        model = Order
        fields = ["id", 'name', 'driver_id', "customer_name", "status", "delivery", "special_instructions", "time_placed", "driver_name", "food_items"]
######################################################################### 

class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField() # Blows my mind that this can relate to a string in the fields sections. It allows you to add/customize  attributes that aren't directly part of the model

    def get_customer_name(self, obj): # self is serializer and obj is the model
        return f"{obj.customer.first_name} {obj.customer.last_name}"
    
    class Meta:
        model = Review
        fields = ["id", "customer_id", "customer_name", "created_date", "content", "likes", "shares"]
# I am pretty sure this doesn't work because there is no way to connect a customer to it currently