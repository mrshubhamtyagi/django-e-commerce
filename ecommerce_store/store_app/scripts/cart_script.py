from store_app.models import ProductModel, CategoryModel, CartModel
from django.contrib.auth.models import User
import random

def add_items():
    # get USER
    users=User.objects.all()
    if not users:
        print("No Users found")
        return
    user = random.choice(users)
        
    
    # get PRODUCT
    products=ProductModel.objects.all()
    if not products:
        print("No products found")
        return
    product=random.choice(products)
    
    # add to CART
    cart_item = CartModel.objects.create(
        user = user,
        product = product,
        quantity = random.randint(1,10), 
    )

    print(f"Item Added - {cart_item.product} | Quantity -{cart_item.quantity}")
    
    
def list_items():
    for item in CartModel.objects.all():
        print(f"User - {item.user} | Product - {item.product} | Quantity -{item.quantity}")  