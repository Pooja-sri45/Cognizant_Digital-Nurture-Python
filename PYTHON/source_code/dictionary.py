def update_employee_data(emp1, emp2):

    if not isinstance(emp1, dict) or not isinstance(emp2, dict):
        print("Invalid dictionary input")
        return

    emp1.update(emp2)

    print("Updated Employee Data:", emp1)


employee1 = {"name": "Pooja", "salary": 50000}
employee2 = {"department": "IT", "city": "Chennai"}

update_employee_data(employee1, employee2)