class Converter:
    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

    def k_to_c(self, k):
        return k - 273.15
converter = Converter()
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice: "))
temp = float(input("Enter temperature: "))
if choice == 1:
    result = converter.c_to_f(temp)
    print("Temperature:", round(result, 2), "F")

elif choice == 2:
    result = converter.f_to_c(temp)
    print("Temperature:", round(result, 2), "C")

elif choice == 3:
    result = converter.c_to_k(temp)
    print("Temperature:", round(result, 2), "K")

elif choice == 4:
    result = converter.k_to_c(temp)
    print("Temperature:", round(result, 2), "C")
else:
    print("Invalid choice")