from django.db import models
from django.utils import timezone
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(null = True, default="", blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(null = True, default="", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    display = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(null = True, default="", blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100, default="")
    text = models.TextField(null = True, default="", blank=True)
    category = models.ForeignKey(Type, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    display = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    email = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title