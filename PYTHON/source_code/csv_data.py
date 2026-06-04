import csv
def process_csv():
    try:
        file = open("emp.csv", "r")
        reader = csv.DictReader(file)
        employees = list(reader)
        file.close()
        
        high_salary = [
            emp for emp in employees
            if int(emp["salary"]) > 50000
        ]

        total = sum(int(emp["salary"]) for emp in employees)
        average = total / len(employees)
        print("Employees with salary > 50000")

        for emp in high_salary:
            print(emp)
        print("\nAverage Salary:", average)

    except FileNotFoundError:
        print("CSV file not found")
    except ValueError:
        print("Invalid data in CSV file")
process_csv()