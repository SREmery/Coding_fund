
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print("Calc options:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Please choose an option (1-4): ")

if choice == "1":
    result = x + y
    print(x, "+", y, "=", result)
elif choice == "2":
    result = x - y
    print(x, "-", y, "=", result)
elif choice == "3":
    result = x * y
    print(x, "x", y, "=", result)
elif choice == "4":
    if y == 0:
        print("Error: cannot continue")
    else:
        result = x / y
        print(x, "/", y, "=", result)
else:
    print("Error: incorrect")