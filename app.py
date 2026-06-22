from inentory import Product, Inventory

inventory = Inventory()
inventory.add_product(Product(1, "TSHIRT", 1000))
inventory.add_product(Product(2, "JEANS", 2000))
inventory.add_product(Product(3, "SHOES", 3000))

print(inventory.check_stock(1))
print(inventory.check_stock(1))


