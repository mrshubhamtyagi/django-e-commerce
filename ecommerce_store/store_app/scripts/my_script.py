from pprint import pprint

from django.db import connection
from store_app.scripts.category_script import add_categories
from store_app.scripts.product_script import add_products
from store_app.scripts.cart_script import add_items, list_items
from store_app.scripts.user_script import create_user, print_users, delete_user


def run():
    print('-----Running My-Script')
    # add_items()

    list_items()
    
    # print_queries()




def print_queries():
    pprint(connection.queries)
    
