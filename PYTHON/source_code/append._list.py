def add_expense(expenses, amount):

    if amount <= 0:
        print("Invalid expense amount")
        return

    expenses.append(amount)

    print("Updated Expenses List:", expenses)

expenses = [1000, 2000, 1500]

add_expense(expenses, 2500)