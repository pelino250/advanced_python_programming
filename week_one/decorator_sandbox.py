from typing import Dict, Any

# students_2 = {
#     "name": "John",
# }
students: Dict[str, Any] = {}


def admin_only(func):
    def wrapper(*args, **kwargs):
        if user_types[user_type] == 1:
            return func(*args, **kwargs)
        else:
            raise ValueError('You are not an admin')

    return wrapper


# function to add student to the dict
@admin_only
def add_student(student_name: str, reg_num: int) -> None:
    students[student_name] = {
        'id': reg_num,
    }


user_types = {
    'student': 3,
    'teacher': 2,
    'admin': 1,
}

name = input('Enter student name: ')
reg_number = int(input('Enter student reg number: '))
user_type = input(f'Choose your user type:  {user_types.keys()}: ')

add_student(name, reg_number)

print(students)
