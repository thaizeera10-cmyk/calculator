
print("Hello world")

x = 10
y = 30
z = x+y
print(z)
x="upcode"
print(x)
print("Hello")
total_score = 98
total_perc = 95.5
student_name = 'thaizeera'
is_selected = True #boolean
print(total_score)
print(total_perc)
print(student_name)
age = 18
print(age, id(age))

age = 20
print(age, id(age))

age1 = "20"
mark = "45"
lab_mark = "10"
total_mark = int(mark)+ int(lab_mark)
print (total_mark)

name = "Thaizeera"
message = "WELCOME UPCODE" + name + "good morning"
age = 37
m = "HEllo. I am {sname}. I am {a}" .format(sname=name, a=age)

print (m)
m1 = f"HEllo. I am {name}. I am {age}"
print(m1)
'''
comment
'''

message2 = "hello" .upper()
print(message2)

message3 = "hello" .lower()
print(message3)
message1 = m.swapcase
print(m)

message1 = len(m)
print(message1)

prod_name = "MENS T SHIRTS AND GIRLS T SHIRTS"

message1 = prod_name.startswith("MENS")
print(message1)
message2 = prod_name.endswith("SHIRTS")
print(message2)

message2 = prod_name.count("SHIRTS")
print(message2)

message2 = prod_name.find("SHIRTS")
print(message2)

message2 = prod_name.split(" ")
print(message2)

phone="7411111111ighj"
message = phone.isnumeric()
print(message)

name="sdsfsf234"
message = name.isalpha()
print(message)

password="sdsfsf234"
message = password.isalnum()
print(message)

students = ["thaizi", "fayaz", "Farzam","Farman"]
student_score = [50,100,80,90]
student_list = list(("farzam", "farman", "faya"))
print(students)
print(student_list)
students[3] = " Farzam"
print(students[3])
students.append("faya")
students.insert(0,"fiya")
print(len(students))
students.remove("faya")
students.reverse()
students.sort()
student_score.sort(reverse=True)
print(students, student_score)


#tuple
#print(type(students))
#students = tuple(("thai", "farzam"))
#student_scores = (50, 45)

#print(students, student_scores, students)

#students_list = []
#students_tuple = ()

#set unordered, duplicate number not allowed

students_set = {"thaizi","farzam"}
name = "jahfar"


if_exist = name in students_set
print(if_exist)
students_set.add("sajeena")

print(students_set)