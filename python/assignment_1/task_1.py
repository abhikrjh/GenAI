products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Monitor"]

sample_product = ("Laptop", 75000, "Electronics")

print(products[1])  # Accessing the second product
print(products[-1])  # Accessing the last product

products.append("Tablet")  # Adding a new product to the list
products.append("Smartwatch")  # Adding another product to the list

print(products)  # Printing the updated list of products

product_list = list(sample_product)  # Converting the tuple to a list
product_list[1] = 70000  # Updating the price of the product
converted_product_tuple = tuple(product_list)  # Converting the list back to a tuple

print(converted_product_tuple)  # Printing the updated product tuple
