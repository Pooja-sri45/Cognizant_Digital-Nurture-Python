class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("Pooja", 50000)
emp2 = Employee("Swetha", 60000)

emp1.display()
emp2.display()