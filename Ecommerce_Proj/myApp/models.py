from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICE = (
    ('CURD','Curd'),
    ('MILK','Milk'),
    ('LASSI','Lassi'),
    ('MILKSHAKE','Milkshake'),
    ('PANEER','Paneer'),
    ('GHEE','Ghee'),
    ('CHEESE','Cheese'),
    ('ICECREAM','Ice-Cream')
)

class Product(models.Model):
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=15)
    product_Image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    
STATE_CHOICES = (
    ('Maharashtra','Maharashtra'),
    ('Goa','Goa'),
    ('Telangana','Telangana'),
    ('Karnataka','Karnataka'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Kerala','Kerala'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Gujarat','Gujarat'),
    ('Odisha','Odisha'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Chhattisgard', 'Chhattishgard'),
    ('Jharkhand', 'Jharkhand'),
    ('Bihar','Bihar'),
    ('Sikkim','Sikkim'),
    ('West Bengal', 'West Bengal'),
    ('Bihar','Bihar'),
    ('Assam','Assam'),
    ('Meghalaya','Meghalaya'),
    ('Tripura','Tripura'),
    ('Mizoram','Mizoram'),
    ('Manipur','Manipur'),
    ('Nagaland', 'Nagaland'),
    ('Arunchal Pradesh','Arunchal Pradesh'),
    ('Nagaland','Nagaland'),
    ('Rajasthan', 'Rajasthan'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Delhi','Delhi'),
    ('Haryana','Haryana'),
    ('Punjab', 'Punjab'),
    ('Uttarakhand','Uttarakhand'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Ladakh','Ladakh')
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length = 45)
    mobile = models.CharField(max_length=12,default = 0)
    pincode = models.IntegerField()
    state = models.CharField(max_length = 120,choices = STATE_CHOICES)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1, null=True)
    totalPrice = models.FloatField(null=True)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length = 100, null = True, blank = True)
    razorpay_payment_id = models.CharField(max_length = 100, null = True, blank = True)
    razorpay_payment_status = models.CharField(max_length = 100, null = True, blank = True)
    paid = models.BooleanField(default='0')

    def __str__(self):
        if self.razorpay_payment_id:
            return f"{self.razorpay_payment_id}"
        else:
            return f"{self.user}"

STATUS_CHOICES = (
    ('ACCEPTED', 'ACCEPTED'),
    ('PACKED','PACKED'),
    ('ON THE WAY', 'ON THE WAY'),
    ('DELIVERED','DELIVERED'),
    ('CANCEL','CANCEL'),
    ('PENDING','PENDING')
)

class Order(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50,choices = STATUS_CHOICES, default = 'PENDING')
    payment = models.ForeignKey(Payment, on_delete = models.CASCADE, default='')
    totalPrice = models.FloatField(null=True)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)