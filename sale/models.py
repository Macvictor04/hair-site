from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    categories = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='item', null=True, blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
class Feedback(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}"
