import json
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"
employees = {}
employees["E101"] = Employee("E101", "Pooja", 50000)
employees["E102"] = Employee("E102", "Swetha", 60000)
data = {}

for emp_id, emp in employees.items():
    data[emp_id] = {
        "name": emp.name,
        "salary": emp.salary
    }
file = open("emps.json", "w")
json.dump(data, file)
file.close()
print("Employee data saved successfully")
file = open("emps.json", "r")
loaded_data = json.load(file)
file.close()
print("\nEmployee Details:")
for emp_id, details in loaded_data.items():
    print(f"ID: {emp_id}, Name: {details['name']}, Salary: {details['salary']}")