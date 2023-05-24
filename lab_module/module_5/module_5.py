from collections import Counter
from typing import List, Union
from random import seed, choice
import requests
import re


PATH_TO_NAMES = "names.txt"
PATH_TO_SURNAMES = "last_names.txt"
PATH_TO_OUTPUT = "sorted_names_and_surnames.txt"
PATH_TO_TEXT = "random_text.txt"
PATH_TO_STOP_WORDS = "stop_words.txt"


def task_1():
    """
    The function open files __'names.txt'__ and __'last_names.txt'__.
    Sorts the names and makes them lowercase. By using `choice` function it assigns random surname to each name.
    Then writes the data to a new file called __'sorted_names_and_surnames.txt'__.
    """
    seed(1)
    with open('names.txt', 'r', encoding="utf-8") as names_file:
        names = names_file.read().splitlines()
    with open('last_names.txt', 'r', encoding="utf-8") as surnames_file:
        surnames = surnames_file.read().splitlines()
    names = sorted([name.lower() for name in names])
    # create a list of random surnames for each name
    surnames_list = [choice(surnames) for _ in range(len(names))]
    # combine and write to a file
    with open('sorted_names_and_surnames.txt', 'w', encoding="utf-8") as data_sorted:
        for name_idx, name in enumerate(names):
            data_sorted.write(names[name_idx] + ' ' + surnames_list[name_idx] + '\n')


def task_2(top_k: int):
    """
    The function reads both `random_text.txt` and `stop_words.txt` files.
    It filters out the stop words and remains only alphabet tokens.
    The number of needed top words is the parameter of function.
    """
    with open('random_text.txt', 'r') as text_file:
        text = text_file.read().lower()
    with open('stop_words.txt', 'r') as words_file:
        stop_words = set(words_file.read().split())
    # regex to extract only the words consisting of alphabet token
    words = re.findall(r'\b[a-z]+\b', text)
    # filter out stop words
    filtered_words = [word for word in words if word not in stop_words]
    word_counts = Counter(filtered_words)
    return word_counts.most_common(top_k)


def task_3(url: str):
    """
    The function takes an url as a parameter and returns the response from the server.
    If the response is successful, it returns the response (url).
    If the response is not successful, it raises an exception.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.RequestException as exc:
        raise requests.RequestException(f"Request failed with error: {str(exc)}")


def task_4(data: List[Union[int, str, float]]):
    """
    The function takes a list of elements as a parameter and returns the sum of all elements, if it is possible.
    It is able to convert strings to float.
    Otherwise, (the character is not a number or not a string), it raises an exception.
    """
    total_sum = 0
    for element in data:
        try:
            # if an element can be converted to a float, it will be converted to a float and added to the total sum
            total_sum += float(element)
        except (ValueError, TypeError):
            raise TypeError("All elements must be numbers (int or float)")
    return total_sum


def task_5():
    """
    The function asks the user to enter two numbers.
    It tries to divide the first number by the second number.
    If the user enters a non-numeric value, it raises a ValueError.
    If the user enters a zero as a second number, it raises a ZeroDivisionError.
    """
    try:
        num1, num2 = input("Enter two numbers: ").split()
        result = float(num1) / float(num2)
        print(result)
    except ValueError:
        print("Entered value is wrong")
    except ZeroDivisionError:
        print("Can't divide by zero")
