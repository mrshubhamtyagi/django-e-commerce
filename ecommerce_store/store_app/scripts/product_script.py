from store_app.models import ProductModel, CategoryModel

def add_products():
    electronics=CategoryModel.objects.get(name='Electronics')
    clothing = CategoryModel.objects.get(name="Clothing")
    home_kitchen = CategoryModel.objects.get(name="Home & Kitchen")
    books = CategoryModel.objects.get(name="Books")
    sports = CategoryModel.objects.get(name="Sports Equipment")

    # Add products for Electronics
    ProductModel.objects.create(
        name='Smartphone',
        description='A high-end smartphone with 128GB storage.',
        price=699, stock=50, category=electronics
    )
    ProductModel.objects.create(name="Laptop", description="A powerful gaming laptop with 16GB RAM.", price=1200, stock=20, category=electronics)
    ProductModel.objects.create(name="Bluetooth Speaker", description="Portable speaker with deep bass.", price=150, stock=30, category=electronics)

    # Add products for Clothing
    ProductModel.objects.create(
        name="T-Shirt", 
        description="Comfortable cotton T-shirt in various sizes.", 
        price=20, stock=100, category=clothing
    )
    ProductModel.objects.create(name="Jeans", description="Stylish denim jeans with a slim fit.", price=40, stock=70, category=clothing)
    
    # Add products for Home & Kitchen
    ProductModel.objects.create(
        name="Cookware Set", 
        description="Non-stick cookware set for everyday cooking.", 
        price=80, stock=15, category=home_kitchen
    )
    ProductModel.objects.create(name="Vacuum Cleaner", description="Powerful vacuum cleaner for home use.", price=200, stock=10, category=home_kitchen)
    ProductModel.objects.create(name="Blender", description="High-speed blender for smoothies and shakes.", price=60, stock=25, category=home_kitchen)
    
    # Add products for Books
    ProductModel.objects.create(
        name="Fiction Book", 
        description="A thrilling mystery novel.", 
        price=10, stock=40, category=books
    )
    ProductModel.objects.create(name="Cookbook", description="A recipe book for quick and easy meals.", price=15, stock=25, category=books)
    ProductModel.objects.create(name="Science Book", description="An informative book on scientific discoveries.", price=25, stock=15, category=books)
    
    # Add products for Sports Equipment
    ProductModel.objects.create(
        name="Football", 
        description="Official size and weight football.", 
        price=30, stock=50, category=sports
    )
    ProductModel.objects.create(name="Tennis Racket", description="Lightweight and durable tennis racket.", price=70, stock=20, category=sports)
    ProductModel.objects.create(name="Yoga Mat", description="Non-slip yoga mat for home workouts.", price=25, stock=35, category=sports)

    print(ProductModel.objects.all())