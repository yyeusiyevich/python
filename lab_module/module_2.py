from itertools import product
from typing import Dict, Any, Tuple, List


def task_1(data_1: Dict[str, int], data_2: Dict[str, int]):
    """The function combines two dictionaries into one, adding the values of the same keys.
    Returns updated dictionary."""
    for key, value in data_2.items():
        if key in data_1:
            data_1[key] += value
        else:
            data_1[key] = value
    return data_1


def task_2():
    """The function creates a dictionary with the keys from 1 to 15 and the values of the square of the keys."""
    empty_dict = {}
    for number in range(1, 16):
        empty_dict[number] = number ** 2
    return empty_dict


def task_3(data: Dict[Any, List[str]]):
    """The function creates all combinations of letters from the values of the dictionary.
    Returns the list of combinations."""
    values = data.values()
    # the product function creates all combinations of letters from the values of the dictionary
    combinations = list(product(*values))
    result = []
    for combination in combinations:
        # a combination is a tuple, so it is converted to a string and added to the list
        result.append(''.join([str(combination[i]) for i in range(len(data.keys()))]))
    return result


def task_4(data: Dict[str, int]):
    """The function finds the highest 3 values of corresponding keys in the dictionary.
    If dictionary has less than 3 keys, the function returns the remaining keys."""
    # create a sorted dictionary by values in descending order and a lambda function as a key
    sorted_dict = sorted(data.items(), key=lambda x: x[1], reverse=True)
    result = [key for key, value in sorted_dict[:3]]
    return result


def task_5(data: List[Tuple[Any, Any]]) -> Dict[str, List[int]]:
    """The function creates a dictionary grouping a sequence of key-value pairs into a dictionary of lists."""
    my_dict = {}
    for key, value in data:
        if key in my_dict:
            my_dict[key].append(value)
        else:
            my_dict[key] = [value]
    return my_dict


def task_6(data: List[Any]):
    """The functions deleted repeated elements from the list."""
    return list(set(data))


def task_7(words: [List[str]]) -> str:
    """The function finds the longest common prefix string amongst an array of strings."""
    # if the words is empty, return an empty string
    if not words:
        return ""
    # create a variable for the first word in the list
    prefix = words[0]
    for string in words[1:]:
        # if the first word is not in the current word, delete the last letter from the prefix
        while not string.startswith(prefix) and (prefix := prefix[:-1]):
            continue
        # if there are no common letters, return an empty string
        if not prefix:
            return ""
    return prefix


def task_8(haystack: str, needle: str) -> int:
    """The function finds the first occurrence of the substring needle in the haystack string.
    If the needle is an empty string, the function returns 0.
    If the needle is not found, returns -1."""
    if not needle:
        return 0
    index = haystack.find(needle)
    return index
