print("Keys: \npress 1 for addition\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division\npress 5 for floor division\npress 6 for modulus\npress 7 for exponentiation\npress 8 to exit")
while True:
    choice = input("Enter your choice: ")
    if choice == '8':
        print("Exiting the calculator. Goodbye!")
        break
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                    
                result = num1 / num2
                print(f"The result of division is: {result}")
            elif choice == '5':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 // num2
                print(f"The result of floor division is: {result}")
            elif choice == '6':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 % num2
                print(f"The result of modulus is: {result}")
            elif choice == '7':
                result = num1 ** num2
                print(f"The result of exponentiation is: {result}") 
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid choice. Please select a valid option from the menu.")    
    