import csv
from datetime import datetime
def analyze_expenses():

    try:
        file = open("expenses.csv", "r")
        reader = csv.DictReader(file)
        category_totals = {}
        current_month = datetime.now().month
        for row in reader:

            expense_date = datetime.strptime(row["date"], "%Y-%m-%d")
            if expense_date.month == current_month:

                category = row["category"]
                amount = float(row["amount"])

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

        file.close()
        print("Expense Summary")

        for category, total in category_totals.items():
            print(f"{category}: {total}")

    except FileNotFoundError:
        print("Expenses file not found")

    except ValueError:
        print("Invalid data in file")

analyze_expenses()