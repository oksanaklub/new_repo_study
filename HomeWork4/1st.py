print(f'Select the number 1')
number_1 = int(input())

print(f'Select the number 2')
number_2 = int(input())
print(f'Select the needed operation (+, -, *, /)')
operation = str(input())

addition = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2

if operation == '+':
    print(addition)
if operation == '-':
    print(subtraction)
if operation == '*':
    print(multiplication)
if operation == '/':
    print(division)



