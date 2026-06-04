import json
students = {}
def add_student(roll_no, name, marks):
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return
    students[roll_no] = {
        "name": name,
        "marks": marks
    }
    print("Student added successfully")
    
def display_students():
    if not students:
        print("No student records found")
        return
    print("\nStudent Records")

    for roll, details in students.items():
        print(f"Roll No: {roll}")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
        print()

def save_records():
    file = open("students.json", "w")
    json.dump(students, file)
    file.close()
    print("Records saved successfully")

add_student(101, "Pooja", 85)
add_student(102, "Swetha", 90)
display_students()
save_records()