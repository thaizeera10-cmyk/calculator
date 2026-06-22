mylist = [91,2,33,4,5,62,7,8,9]
#filter

mylist.sort()
mylist.sort(reverse=True)
print(mylist)


products = [ 
    
    
def sort_by_price(p):
  return p["price"]
products.sort(key=sort_by_price, reverse= True)
print(products)
    
    
    products.sort(key=)
]

def even_number_func(n):
    return (n % 2) == 0
even_numbers = list(filter(even_number_func, mylist))
print(even_numbers)


odd_numbers = list(filter(lambda n: (n %2 ) !=0, mylist))
print(odd_numbers)