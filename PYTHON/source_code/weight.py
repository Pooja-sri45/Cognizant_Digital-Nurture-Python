
def convert_weight():

    try:
        kg = float(input("Enter weight in kilograms: "))

        if kg <= 0:
            print("Invalid weight")
            return

        lbs = kg * 2.20462
        print(f"Weight in pounds: {lbs:.2f}")

    except ValueError:
        print("Please enter a valid decimal number")

convert_weight()