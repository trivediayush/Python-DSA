def calculate(num1, num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        return None
    else:
        print(f"The result of {num1} divided by {num2} is {result}.")
        return result

calculate(10, 2)