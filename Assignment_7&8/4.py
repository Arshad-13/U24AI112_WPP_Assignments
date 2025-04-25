# Create a class "Employee" with attributes name and salary. Implement overloaded operators +
# and - to combine and compare employees based on their salaries.

class Employee:
    def __init__(self):
        self.name = None
        self.salary = None

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary > other.salary

emp1 = Employee()
emp1.name = "Arshad"
emp1.salary = 50000

emp2 = Employee()
emp2.name = "Manthan"
emp2.salary = 60000

print(emp1 + emp2)
print(emp1 - emp2)