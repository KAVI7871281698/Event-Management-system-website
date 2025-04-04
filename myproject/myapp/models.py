from django.db import models
from django.core.validators import RegexValidator
import datetime

# Create your models here.

class register_table(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,primary_key=True)
    password=models.CharField(max_length=10)
    address = models.TextField(null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed."
    )
    mobile = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)

class cateringservice(models.Model):
    CATERING_CHOICES = [
        ('Simple', 'Simple (6-8 item    s)'),
        ('Standerd', 'Standard (10-12 items)'),
        ('Premium', 'Premium (15-20 items)'),
    ]
    
    TYPE_CHOICES = [
        ('veg', 'Veg'),
        ('non-veg', 'Non-Veg'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    catering_package = models.CharField(max_length=20, choices=CATERING_CHOICES)
    catering_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    event_date = models.DateField()
    description = models.TextField(blank=True, null=True)

class package(models.Model):
    package_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    features = models.TextField(blank=True, null=True)

class order(models.Model):
   name=models.CharField(max_length=20, null=True)
   email = models.CharField(max_length=50, null=True)
   plans = models.CharField(max_length=50) 
   location = models.TextField(null=True) 
   event_date = models.DateTimeField(null=True)
   event_name = models.CharField(max_length=50, null=True)
   features = models.TextField(null=True) 
   event = models.ForeignKey(package, on_delete=models.CASCADE)  
   order_date = models.DateTimeField(auto_now_add=True) 
   order_month = models.CharField(max_length=10, default=datetime.datetime.now().strftime('%B'), editable=False)  # Example: "February"
   order_year = models.IntegerField(default=datetime.datetime.now().year, editable=False)  # Example: 2025

class reviews(models.Model):
    name=models.CharField(max_length=20)
    reviews=models.CharField(max_length=200)  
