class Product:
    def __init__(self, name, id, title, price, stock_count):
        self.name = name
        self.id = id
        self.title = title
        self.price = price
        self.stock_count = stock_count

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def check_stock(self, product_id):
        for p in self.products:
            if p.id == product_id:
                return p.stock_count
            
        return 0
    def update_stock(products, product_id, quantity):
        for p in products:
            if p.id == product_id:
                p.stock_count = p.stock_count + quantity

                return True
            return False
        