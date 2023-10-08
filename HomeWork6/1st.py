from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade'])

students_list = [
    Student(name='Alice', age=20, grade=90),
    Student(name='Bob', age=25, grade=85),
    Student(name='Charlie', age=22, grade=80),
]

expected_types = (str, int, int)

for i, student in enumerate(students_list, start=1):
    print(f"Student {i}:")
    for idx, (field, expected_type) in enumerate(zip(student, expected_types), start=1):
        if not isinstance(field, expected_type):
            print(f"Warning! Invalid data type for {Student._fields[idx-1]}. "
                  f"Expected {expected_type.__name__}, Actual {type(field).__name__}")
        else:
            print(f"{Student._fields[idx-1]}: {field}")
    print()
