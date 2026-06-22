class product:
    def __init__(self,_id, _title, price, category, manufacture):
        self.id = _id
        self.title = _title
        self.price = price
        self.category = category
        self.manufacture = manufacture
        self.warranty_end_date = ""

    def display_details(self):
        print(f"{self.title}: {self.price}")

p1= product(1, "casio watch", 5000, "watch", "casio")
p1.warranty_end_date = "12/12/2025"
p1.display_details()
p2= product(2, "IPHONE 15", 80000, "mobile", "apple")

print(p1.title, p1.warranty_end_date)
print(p2.title)

#inheritance:
class ELectonicsProduct(product):
    def __init__(self, _id, _title, price, category, manufacture, warranty, purchase_date, rechargeable):
        super().__init__(_id, _title, price, category, manufacture)
        self.warranty = warranty
        self.purchase_date = purchase_date
        self.rechargeable = rechargeable

IPHONE = ELectonicsProduct(2, "IPHONE 15", 80000, "mobile", "apple", "1 year", "12/12/2023", True)

IPHONE.display_details()