import time
from typing import List


Matrix = List[List[int]]


def task_1(exp: int):
    """The function returns a function that raises the base to the power of exp."""
    def power(base):
        return base ** exp
    return power


def task_2(*args, **kwargs):
    """The function accepts any number of positional and keyword arguments and prints them in
    the order in which they were passed to the function."""
    for arg in args:
        print(arg)
    for value in kwargs.values():
        print(value)


def helper(func):
    """The decorator accepts a function and prints a greeting and a farewell message before and
    after the function call. Returns the result of the function call."""
    def wrapper(*args, **kwargs):
        print("Hi, friend! What's your name?")
        result = func(*args, **kwargs)
        print("See you soon!")
        return result
    return wrapper


@helper
def task_3(name: str):
    print(f"Hello! My name is {name}.")


def timer(func):
    """The decorator accepts a function and prints the time it took to execute the function. Returns
    the result of the function call."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
    return wrapper


@timer
def task_4():
    return len([1 for _ in range(0, 10 ** 8)])


def task_5(matrix: Matrix) -> Matrix:
    """The function accepts a matrix and returns its transpose."""
    # get number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    # initialize a new matrix with flipped dimensions
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    # iterate over original matrix and fill in the transposed matrix
    for row in range(rows):
        for column in range(cols):
            transposed[column][row] = matrix[row][column]
    return transposed


def task_6(queue: str):
    """The function accepts a string that contains only parentheses and returns True if the
    parentheses are balanced and False otherwise."""
    stack = []
    # if the character is an opening parenthesis, push it to the stack
    for char in queue:
        if char == "(":
            stack.append(char)
            # if the character is a closing parenthesis, check if the stack is empty
        elif char == ")":
            # if the stack is empty, the parentheses are not balanced, return False
            if not stack:
                return False
            # and if the stack is not empty, pop the top element (it should be an opening parenthesis)
            stack.pop()
    # after iterating over the string, if the stack is empty, the parentheses are balanced, return True
    # otherwise, the parentheses are not balanced, return False
    return not stack

