from datetime import datetime
class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def display(self):
        print(f"Task: {self.name}")
        print(f"Due Date: {self.due_date.date()}")
        print(f"Priority: {self.priority}")
        print()
tasks = []
tasks.append(Task("Python Assignment", "2026-06-10", "High"))
tasks.append(Task("Mini Project", "2026-06-05", "Medium"))
tasks.append(Task("Record Submission", "2026-06-01", "Low"))
tasks.sort(key=lambda x: x.due_date)
today = datetime.now()
print("Task Schedule\n")
for task in tasks:
    task.display()
    if task.due_date < today:
        print("Status: Overdue\n")
    else:
        print("Status: Upcoming\n")