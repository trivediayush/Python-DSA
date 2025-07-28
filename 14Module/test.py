import calcy

Addition_result = calcy.add(5,4)
Subtraction_result = calcy.subtract(10, 5)
Multiplication_result = calcy.multiply(3, 7)    
Division_result = calcy.divide(20, 4)

print(f'Addition: {Addition_result}')
print(f'Subtraction: {Subtraction_result}')
print(f'Multiplication: {Multiplication_result}')
print(f'Division: {Division_result}')
print(f'Division by zero: {calcy.divide(5, 0)}')