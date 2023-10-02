list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisor = int(input("Введіть число: "))
print(f"Числа, які діляться на {divisor} зі списку:")

for num in list_of_numbers:
    if num % divisor == 0:
        print(num)
