print("hello")




#name= input("Enter your name:  ")
#print(name)

#n1= int(input("Enter first number:   "))

#n2= int(input("Enter second number:  "))

#result = n1 + n2

#rint(result)

#function definition

def add_two_numbers(x,y):
    f_number = int(x)
    s_number = int(y)
    sum = f_number + s_number
    return sum
#print(f_number)

#function call
r1 = add_two_numbers(122,233)
print(r1)

r3 = add_two_numbers(x=400, y=600)
print(r3)

numbers = [12, 32 ,23,34]
result = sum(numbers)
print(result)


def greet(name, message):
    print(f"{message} {name}")


greet("thaizi", "Hello")



#lambda functions

multiply = lambda a,b: a*b
print(multiply(a=40, b=20))