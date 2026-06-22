# Create empty shopping list
shopping_list = []


# Add item function
def add_item(item):
    shopping_list.append(item)
    print(item["title"], "added to shopping list")


# Remove item function
def remove_item(title):
    for item in shopping_list:
        if item["title"] == title:
            shopping_list.remove(item)
            print(title, "removed from shopping list")
            return

    print(title, "not found")


# Show shopping list
def show_list():
    print("\nShopping List:\n")

    if len(shopping_list) == 0:
        print("Shopping list is empty")

    else:
        for item in shopping_list:
            print("ID:", item["id"])
            print("Title:", item["title"])
            print("Price:", item["price"])
            print("Category:", item["category"])
            print("Rating:", item["rating"]["rate"])
            print("------------------------")


# Products from Fake Store API
products = [
    {
        "id": 1,
        "title": "Fjallraven Backpack",
        "price": 109.95,
        "category": "men's clothing",
        "rating": {"rate": 3.9}
    },
    {
        "id": 2,
        "title": "Mens Casual Premium T-Shirts",
        "price": 22.3,
        "category": "men's clothing",
        "rating": {"rate": 4.1}
    },
    {
        "id": 3,
        "title": "Mens Cotton Jacket",
        "price": 55.99,
        "category": "men's clothing",
        "rating": {"rate": 4.7}
    },
    {
        "id": 4,
        "title": "Mens Casual Slim Fit",
        "price": 15.99,
        "category": "men's clothing",
        "rating": {"rate": 2.1}
    },
    {
        "id": 5,
        "title": "Dragon Chain Bracelet",
        "price": 695,
        "category": "jewelery",
        "rating": {"rate": 4.6}
    }
]


# Manually add items
add_item(products[0])
add_item(products[1])
add_item(products[2])
add_item(products[3])
add_item(products[4])

# Show list
show_list()

# Remove item
remove_item("Mens Cotton Jacket")

# Show updated list
show_list()