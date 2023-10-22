def new_function(num_1, num_2, action):
    if action == '+':
        print(num_1 + num_2)
    elif action == '-':
        print(num_1 - num_2)
    elif action == '*':
        print(num_1 * num_2)
    elif action == '/':
        print(num_1 / num_2)
    else:
        print(f'Not known operation: {action}')


print(f'Select the number 1')
number_1 = int(input())

print(f'Select the number 2')
number_2 = int(input())

print(f'Select the needed operation (+, -, *, /)')
operation = str(input())

new_function(num_1=number_1, num_2=number_2, action=operation)
