course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

try:
    key = input("Enter the key: ")
    value = course[key]
    print( f"Key value '{key}': {value}")
except KeyError:
    print(f"Key '{key}' does not exist")
