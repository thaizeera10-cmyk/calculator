#looping
orders = [1200,400,200]
for order in orders:
    tax = order + 10/100
    print(f"Order amount:{order}, TAX:{tax}")


comp_name = "upcode"

for l in comp_name:
    print(l)

prod = {
    "id":1,
    "title":"T shirt"
}


for key,value in prod.items():
    print(f"{key}:{value}")


for v in prod.values():
    print(v)

products = [
    {
        "id":1,
        "title":"T shirt"
    
    },
    {
        "id":2,
        "title":"Bag"
    }
]

for p in products:
    print(f"{p['title']}")