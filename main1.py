#conditional statement

total_perc = int(input("Enter your degree total percentage"))


message = ""
if total_perc >= 75:
    message = "EXCELLENT"
elif total_perc <75 and total_perc >= 50:
    message = "GOOD"
else:
    message = "need improvment"

print(message)

name = ""
if name:
    print(name)
else:
    print("name is empty")
