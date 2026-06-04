
def next_year_age():

    try:
        
        age = int(input("Enter your age: "))

        if age < 0:
            print("Invalid age")
            return

        print(f"Next year you'll be {age + 1}")

    except ValueError:
        print("Please enter a valid number")

next_year_age()
