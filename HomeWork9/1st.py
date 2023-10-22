with open("test.txt", "r") as source_file:
    data = source_file.read()

with open("test2.txt", "w") as target_file:
    target_file.write(data)
