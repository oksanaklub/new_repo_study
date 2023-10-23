def is_prime(number):
    if number < 2 or number > 1000:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


print(f'Select the number')
num = int(input())

result = is_prime(num)
print(f"{num} is prime: {result}")
