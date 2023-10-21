a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

elements_not_in_b = []

for element in a:
    if element not in b:
        elements_not_in_b.append(element)

print("Unique elements which exists in list a", elements_not_in_b)
