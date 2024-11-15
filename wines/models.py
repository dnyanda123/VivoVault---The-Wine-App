from django.db import models
from django.contrib.auth.models import User

class Wine(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    type = models.CharField(max_length=50)
    vintage_year = models.PositiveIntegerField()
    region = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    serving_temperature = models.CharField(max_length=50, default="")
    Alcohol = models.CharField(max_length=50, default="")
    Bottle_size = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.vintage_year})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
