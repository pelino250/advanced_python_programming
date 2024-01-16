# Python annotation:
#   - A way to attach metadata to a function's parameters and return value
#   - A way to attach metadata to class attributes and methods
#   - A way to attach metadata to module-level code

# Annotations are stored in the __annotations__ attribute of the function
# Annotations are not enforced by Python interpreter
# Annotations are not a type hint

# examples
def my_func(a: str, b: int) -> str:
    return a * b


print(my_func.__annotations__)


# python annotations uses:

# 1 - documentation
# example of documentation:
def repeat_string(s: str, n: int) -> str:
    """Repeat string s, n times"""
    return s * n


# print(repeat_string("Hello", 3))


# 2 - Validation
def validate(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for arg, annotation in zip(args, annotations.values()):
            if not isinstance(arg, annotation):
                raise ValueError(f'Argument {arg} is not of expected type {annotation}')
        return func(*args, **kwargs)

    return wrapper

@validate
def repeat_string(s: str, n: int) -> str:
    return s * n


try:
    print(repeat_string(3, '3'))  # Raises ValueError
except ValueError as e:
    print(e)


# def test_func(a:str):
#     return 1
#
# def test_func(a:int):
#     return '1'

# 3  - function overloading
# # example of function overloading:
# def my_func(a: str, b: int) -> str:
#     return a * b
#
# def my_func(a: int, b: int) -> int:
#     return a + b


# 4 - dependency injection / framework:

# 5 - serialization / deserialization
