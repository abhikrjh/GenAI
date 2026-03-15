products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Monitor"]

price_dict = {
    "Laptop": 75000,
    "Mobile": 40000,
    "Headphones": 3000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

categories = ["Electronics", "Electronics", "Audio", "Accessories", "Accessories", "Electronics"]

# Create catalog
catalog = []

# Create catalog
catalog = []

for i in range(len(products)):
    product_name = products[i]
    price = price_dict[product_name]
    category = categories[i]

    catalog.append((product_name, price, category))

print("Catalog:", catalog)

category_to_products = {}

for product, price, category in catalog:

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print("Category to products:", category_to_products)

max_category = max(category_to_products, key=lambda x: len(category_to_products[x]))

print("Category with maximum products:", max_category)

print("Products in that category:")
for product in category_to_products[max_category]:
    print(product)