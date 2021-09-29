from django.db import models
from django.contrib.auth import get_user_model 

User = get_user_model()

class Category(models.Model):
    category = models.CharField(max_length=127)
    def __str__(self):
        return self.category

class Appliances(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='appliances')
    brand = models.CharField(max_length=127, default='')
    model = models.CharField(max_length=127, default='')
    price = models.DecimalField(decimal_places=2, max_digits=15, default=0.00)
    quantity = models.PositiveIntegerField(default=0)
    inStock = models.BooleanField(default=True)

    def __str__(self):
        return self.brand + self.model

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    appliances = models.ForeignKey(Appliances, on_delete=models.CASCADE, related_name='comment_appliance')
    text = models.TextField(max_length=1023, default='')
    posted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author.username + self.appliances.brand 