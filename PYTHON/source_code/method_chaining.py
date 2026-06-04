class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):

        if salary > 0:
            self.salary = salary
        return self

    def apply_raise(self, amount):

        if amount > 0:
            self.salary += amount
        return self

    def display(self):
        print("Employee Name:", self.name)
        print("Final Salary:", self.salary)

emp = Employee("Poojasri")
emp.set_salary(50000).apply_raise(5000).display()