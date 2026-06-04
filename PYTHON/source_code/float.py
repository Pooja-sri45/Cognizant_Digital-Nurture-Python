# Function to calculate net salary
def calculate_net_salary(salary, tax_rate):
    
    if salary <= 0:
        print("Invalid salary")
        return

    if tax_rate < 0 or tax_rate > 1:
        print("Invalid tax rate")
        return

    tax = salary * tax_rate
    net_salary = salary - tax
    print(f"Net Salary: {net_salary:.2f}")

salary = 75000.5
tax_rate = 0.18


calculate_net_salary(salary, tax_rate)