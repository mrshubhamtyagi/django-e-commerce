from store_app.models import CategoryModel

def add_categories():
    CategoryModel.objects.create(
        name="Electronics", 
        description="Devices, gadgets, and more."
    )
    CategoryModel.objects.create(name="Clothing", description="Men's and women's clothing.")
    CategoryModel.objects.create(name="Home & Kitchen", description="Appliances and utensils.")
    CategoryModel.objects.create(name="Books", description="Fiction, non-fiction, and more.")
    CategoryModel.objects.create(name="Sports Equipment", description="Gear for all kinds of sports.")

    # Verify the categories
    CategoryModel.objects.all()