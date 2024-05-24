from django.db import models
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=45, blank = True)
    password= models.CharField(max_length=50, blank = True)
    email = models.EmailField(blank = True, null=True) # Interesting bug that blank emails are not unique and only one can be set to blank
    address = models.CharField(max_length=100, blank = True)
    city = models.CharField(max_length=70, blank = True) 
    state = models.CharField(max_length=2, blank = True)
    zipcode = models.CharField(max_length=5, blank = True)
    phone = models.CharField(max_length=10, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

STATUS = (
    ("Received", "Received"),
    ("Being Made", "Being Made"),
    ("Done", "Done"),
    ("Picked Up", "Picked Up"),
    ("On Its Way", "On Its Way"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled")
)

CATEGORY = (
    ("Starters", "Starters"),
    ("Breakfast", "Breakfast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),
    ("Drinks", "Drinks"),
    ("Desserts", "Desserts")
)

SPICINESS = (
    ("Not Applicable", "Not Applicable"),
    ("Mild", "Mild"),
    ("Medium", "Medium"),
    ("Hot", "Hot"),
    ("Burn Yo Butthole", "Burn Yo Butthole"),
)

class Driver(models.Model):
    name = models.CharField(max_length=20)
    car_color = models.CharField(max_length=15)
    car_make = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"
    
class FoodItem(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    desc = models.CharField(max_length=500)
    price = models.CharField(max_length=6, null=True)
    qty = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name} {self.price}"

class Order(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, blank=True, null=True)
    delivery = models.BooleanField(default=False, blank=True, null=True)
    special_instructions = models.TextField(max_length=1000, blank=True, null=True)
    time_placed = models.DateTimeField(auto_now_add=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, verbose_name="Driver", blank=True)
    food_items = models.ManyToManyField(FoodItem, through="Order_Details")

    def __str__(self):
        return f"{self.name.first_name} {self.name.last_name} {self.time_placed}"


class Order_Details(models.Model):
    food_id = models.ForeignKey(FoodItem, on_delete=models.SET_NULL, null=True) # verbose_name="Menu Item"
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    qty = models.SmallIntegerField()
    tag = models.CharField(max_length=20, blank=True)
    spiciness = models.CharField(max_length=20, choices=SPICINESS, null=True)
    special_instructions = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.food_id.name} x {self.qty}"


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    likes = models.PositiveSmallIntegerField()
    shares = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.customer.first_name}"

