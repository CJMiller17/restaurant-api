from django.db import models
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=45, unique=True)
    password= models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    phone = models.CharField(max_length=10, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return

STATUS = (
    ("Received", "Received"),
    ("Being Made", "Being Made"),
    ("Done", "Done"),
    ("Picked Up", "Picked Up"),
    ("On Its Way", "On Its Way"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled")
)

class Driver(models.Model):
    name = models.CharField(max_length=20)
    car_color = models.CharField(max_length=15)
    car_make = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)

    def __repr__(self):
        return

class Order(models.Model):
    name = f"{Customer.first_name} {Customer.last_name}"
    status = models.CharField(max_length=20, choices=STATUS)
    delivery = models.BooleanField(default=False)
    special_instructions = models.TextField(max_length=1000)
    time_placed = models.DateTimeField(auto_now_add=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return 

class FoodItem(models.Model):
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=500)
    qty = models.SmallIntegerField()

    def __repr__(self):
        return

class Order_Details(models.Model):
    food_id = models.ForeignKey(FoodItem, on_delete=models.SET_NULL, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    qty = models.SmallIntegerField()
    tag = models.CharField(max_length=20)
    spiciness = models.TextField()
    special_instructions = models.CharField(max_length=500)

    def __repr__(self):
        return


class Review(models.Model):
    customer = models.ForeignKey( Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    likes = models.PositiveSmallIntegerField()
    shares = models.PositiveSmallIntegerField()

    def __repr__(self):
        return