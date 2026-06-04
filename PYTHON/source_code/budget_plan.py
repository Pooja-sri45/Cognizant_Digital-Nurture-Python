import matplotlib.pyplot as plt
class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0
    def add_expense(self, amount):
        self.spent += amount
    def check_budget(self):
        if self.spent > self.limit:
            print(f"Alert: {self.name} budget exceeded!")
    def display(self):
        print(f"{self.name}")
        print(f"Budget Limit: {self.limit}")
        print(f"Amount Spent: {self.spent}")
        print()
food = Category("Food", 3000)
travel = Category("Travel", 5000)
shopping = Category("Shopping", 4000)
food.add_expense(3500)
travel.add_expense(2500)
shopping.add_expense(4500)
categories = [food, travel, shopping]
print("Monthly Budget Summary\n")
for category in categories:
    category.display()
    category.check_budget()
labels = [c.name for c in categories]
amounts = [c.spent for c in categories]

plt.pie(amounts, labels=labels, autopct='%1.1f%%')
plt.title("Monthly Expense Distribution")
plt.show()