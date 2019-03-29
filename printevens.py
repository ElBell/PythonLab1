from numbers import Number
from typing import List


def print_even(input_list: List[int]):
    new_list: List[int] = []
    for number in input_list:
        if number % 2 == 0 and number <= 237:
            new_list.append(number)
        if number > 237:
            break
    print(new_list)
    return new_list
