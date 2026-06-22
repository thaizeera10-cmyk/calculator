# Parent Class
class Employee:
    def __init__(self, emp_id, name, place, address, phone):
        self.emp_id = emp_id
        self.name = name
        self.place = place
        self.address = address
        self.phone = phone

    def display(self):
        print("Employee Details")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Place:", self.place)
        print("Address:", self.address)
        print("Phone:", self.phone)


# Child Class 1 - Permanent Employee
class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, place, address, phone,
                 joining_date, designation, salary):

        super().__init__(emp_id, name, place, address, phone)
        self.joining_date = joining_date
        self.designation = designation
        self.salary = salary

    def display(self):
        super().display()
        print("Joining Date:", self.joining_date)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


# Child Class 2 - Contract Employee
class ContractEmployee(Employee):
    def __init__(self, emp_id, name, place, address, phone,
                 start_date, contract_end_date, hourly_rate):

        super().__init__(emp_id, name, place, address, phone)
        self.start_date = start_date
        self.contract_end_date = contract_end_date
        self.hourly_rate = hourly_rate

    def display(self):
        super().display()
        print("Start Date:", self.start_date)
        print("Contract End Date:", self.contract_end_date)
        print("Hourly Rate:", self.hourly_rate)



# Permanent Employee object
emp1 = PermanentEmployee(
    101, "John Doe", "New York", "123 Street NY", "1234567890",
    "2020-01-15", "Software Engineer", 80000
)

emp2 = ContractEmployee(
    201, "Jane Smith", "California", "456 Avenue CA", "9876543210",
    "2024-01-01", "2024-12-31", 50
)

# Output
emp1.display()
print("\n-----------------\n")
emp2.display()