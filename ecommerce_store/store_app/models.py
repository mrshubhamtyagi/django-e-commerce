from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name;
    
    
    
class ProductModel(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True, null=True)
    price=models.PositiveIntegerField()
    stock=models.PositiveSmallIntegerField()
    category=models.ForeignKey(
        CategoryModel, 
        on_delete=models.CASCADE,
        # related_name='products'
    )
    image=models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.stock > 0
    


class CartModel(models.Model):
    quantity=models.PositiveSmallIntegerField(default=1)
    added_at=models.DateTimeField(auto_now_add=True)
    product=models.ForeignKey(
        ProductModel, 
        on_delete=models.CASCADE,
        related_name='cart_items'
    )
    user= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts'
    )
    
    def __str__(self):
        product_name = self.product.name
        quality = f'x{self.quantity}'
        user_name = self.user.username if self.user else "User Unknown"
        return f"{product_name} ({quality}) | {user_name}"

    @property
    def total_price(self):
        return self.quantity * self.product.price
    