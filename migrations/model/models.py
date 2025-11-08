from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class User(models.Model):
    name = models.CharField(max_length=80, null=False, validators=[MinLengthValidator(3)])
    age = models.IntegerField(null=False, validators=[MinValueValidator(5), MaxValueValidator(100)])
    description = models.TextField(blank=True, default=":)")

    def __str__(self):
        return self.name

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(null=False, max_length=200, validators=[MinLengthValidator(3)])
    price = models.IntegerField(null=False, default=0)
    description = models.TextField(default=":}", max_length=1000)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.price}$"
    
class companie(models.Model):
    name = models.CharField(null=False, max_length=100, validators=[MinLengthValidator(2)])
    founded_year = models.IntegerField(null=False, validators=[MinValueValidator(1800), MaxValueValidator(2025)])
    website = models.URLField(blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name