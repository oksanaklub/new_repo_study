def square():
    for el in range(0, 1000000001, 2):
        yield el ** 2


gen = square()
print(next(gen))
print(next(gen))
print(next(gen))
