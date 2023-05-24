from numbers import Number
from typing import List, Any


def task_1():
    """The function returns list of correct numbers between 1 and 1000 (both included)
    that are divisible by 3 and multiple of 5."""
    # range function generates a list of numbers between 1 and 1000
    # the first condition checks whether i (a number) is divisible by 3
    # (i.e., whether the remainder of i divided by 3 is zero)
    # the second condition checks whether i is a multiple of 5 (i.e., whether the remainder of i divided by 5 is zero)
    return [i for i in range(1, 1001) if i % 3 == 0 and i % 5 == 0]


def task_2(queue: str):
    """The function accepts a string and calculates the number of digits and letters (English) in the string,
    and returns the count of digits and letters as a tuple"""
    # two variables are used to store the number of digits and letters in the string
    digits_cnt = 0
    letters_cnt = 0
    # a loop iterates over each character in the input string and increment appropriate variable by 1
    for char in queue:
        if char.isdigit():
            digits_cnt += 1
        elif char.isalpha():
            letters_cnt += 1
    return digits_cnt, letters_cnt


def task_3(data_1: List[Any], data_2: List[Any]):
    """The function computes the difference between two lists and returns the tuple of differences."""
    # set function makes easier to perform mathematical operations on the lists
    difference12 = list(set(data_1) - set(data_2))
    difference21 = list(set(data_2) - set(data_1))
    return difference12, difference21


def task_4(values: List[int]) -> int:
    """The function converts a list of multiple integers(non-negative) into a single integer"""
    #  initialize an empty string called result, which will be used to build the resulting integer
    result = ""
    # a loop iterates over each integer in the input list
    for i in values:
        # append the string representation of the current integer to the result string.
        result += str(i)
    # return the integer equivalent of the result string using the int() function
    return int(result)


def task_5(batches: List[List[Number]]) -> List:
    """The function finds the list in a list of lists whose sum of elements is the highest.
    If the nested lists have the same max sum, then you need to return first of them."""
    # initialize variables that will track of the maximum sum and the corresponding list
    max_sum = -float('inf')
    max_list = []
    # a loop iterates over each list in the input list of lists
    for lst in batches:
        # calculate the sum of the elements in the current list
        current_sum = sum(lst)
        # check if the current sum is greater than the current maximum sum
        # if it is, then the max_sum and max_list variables are updated
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = lst
    return max_list


def task_6(value: int) -> int:
    """The function reverses integer without usage of converting to str."""
    # variables will be used to store the reversed value and the sign of the input value
    reversed_value = 0
    sign = 1 if value >= 0 else -1
    # convert the input value to its absolute value, which allows the function to work with negative values as well
    value = abs(value)
    #  a loop continues as long as there are still digits in the input value
    while value > 0:
        # the last digit of the input value is extracted using the modulo operator
        remainder = value % 10
        # the last digit is added to the reversed value
        reversed_value = reversed_value * 10 + remainder
        # the last digit is removed from the input value
        value //= 10
    return sign * reversed_value


def task_7(string: str):
    """The function finds the first non-repeating character in given string.
    Returns this symbol if it's existed. Otherwise, None returned."""
    # a dictionary is used to store the count of each character in the input string
    char_cnt = {}
    # a loop iterates over each character in the input string
    for char in string:
        # if the character is already in the dictionary, then its count is incremented by 1 using the get() method
        char_cnt[char] = char_cnt.get(char, 0) + 1
    # a loop iterates over each character in the input string
    for char in string:
        # if the count of the current character is 1, then it is returned
        if char_cnt[char] == 1:
            return char
    # if no non-repeating character is found, then None is returned
    return None


def task_8(values: List[int]):
    """ The function takes a list of integers as an input parameter. Returns a new list such that each element
    at index i of the new list is the product of all the numbers in the original array except the one at i."""
    # if the input list has only one element, the function simply returns the input list (the numnber)
    val_length = len(values)
    if val_length == 1:
        return values
    # initialize as lists of length n containing only ones.
    left_product = [1] * val_length
    right_product = [1] * val_length
    # calculate the left product of each element in the input list
    for i in range(1, val_length):
        left_product[i] = left_product[i - 1] * values[i - 1]
    # calculate the right product of each element in the input list
    for i in range(val_length - 2, -1, -1):
        right_product[i] = right_product[i + 1] * values[i + 1]
    # return a list where each element at index i is the product of the left and right products
    # calculated for the same index in the input list
    return [left_product[i] * right_product[i] for i in range(val_length)]

