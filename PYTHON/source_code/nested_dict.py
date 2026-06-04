def get_salary(data, department, employee):

    if department not in data:
        print("Department not found")
        return

    if employee not in data[department]:
        print("Employee not found")
        return

    print("Employee Salary:", data[department][employee])

employees = {
    "IT": {
        "Pooja": 50000,
        "Swetha": 60000
    },
    "HR": {
        "Vasan": 45000
    }
}

get_salary(employees, "IT", "Pooja")