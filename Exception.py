try:
    # Code that might raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

except ZeroDivisionError:
    # Handle the specific exception for division by zero
    print("Error: Division by zero is not allowed.")

except ValueError:
    # Handle the exception for invalid input (e.g., non-integer)
    print("Error: Invalid input. Please enter valid numbers.")

except Exception as e:
    # Handle all other exceptions
    print(f"An error occurred: {e}")

else:
    # Code to be executed if no exception is raised
    print(f"The result of the division is: {result}")

finally:
    # Code that runs regardless of whether an exception was raised or not
    print("Execution completed.")
