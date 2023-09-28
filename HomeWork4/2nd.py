first_name_input = input("Type you name: ")
reversed_first_name_input = first_name_input[::-1]

if first_name_input == reversed_first_name_input:
    print(f"String {first_name_input} is Palindrome ")
else:
    print(f"String {first_name_input} is not Palindrome ")