from django.db import models

# Create your models here.

class Product(models.Model):
    """this is the model for the product in our store"""
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='product_image', default='prod.jpg')
    cost = models.IntegerField(blank=True)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name