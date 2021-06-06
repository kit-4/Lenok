from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
import uuid

class Picture(models.Model):
    """A class representing a piece of art
    """

    title = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=1000)

    height = models.FloatField(validators=[MaxValueValidator(100000)])
    width = models.FloatField(validators=[MaxValueValidator(100000)])
    materials = models.CharField(max_length=100)

    gallery = models.CharField(blank=True, null=True, max_length=100)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)

    is_in_works = models.BooleanField(default=False)
    is_in_color = models.BooleanField(default=False)
    is_in_graphics = models.BooleanField(default=False)

    SOLD_STATUS = (
            ('a', 'Available'),
            ('u', 'Undefined Price'), #no price, but for sale
            ('r', 'Reserved'),
            ('s', 'Sold'),
            ('n', 'NotForSale'),
    )

    status = models.CharField(
            max_length=1,
            choices=SOLD_STATUS,
            blank=True,
            default='a',
    )

    image = models.ImageField(upload_to='images')

    picture_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Customer(models.Model):
    deviceId= models.CharField(max_length=200, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # fill this fields in checkout page
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.deviceId
        return str(name)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'order ' + self.customer.deviceId

    def get_total(self):
        total = 0
        for item in self.orderitem_set.all():
            total += item.picture.price
        return total


class OrderItem(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.SET_NULL,
            null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
            null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
            blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
            blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Project(models.Model):
    """A class representing a project (exhibition)
    """

    title = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=100000)

    gallery = models.CharField(blank=True, null=True, max_length=100)

    image = models.ImageField(upload_to='images')
    link_name = models.CharField(blank=False, null=False, max_length=100)
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
