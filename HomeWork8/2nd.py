roles = {
    'admin': ['Oksa', 'Pavlik'],
    'maintainer': ['Cat', 'Dog'],
    'manager': ['Eve', 'Leo'],
    'developer': ['Lui', 'Henry']
}

user_name = input("Enter your name: ")

user_role = 'Guest'

for role, users in roles.items():
    if user_name in users:
        user_role = role
        break

print(f"Hello, {user_role}")
