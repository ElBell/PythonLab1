from numbers import Number
from typing import List, Any


def largest_element(input_list: List[Any]) -> Any:
    return max(input_list)


def reverse_list(input_list: List[Any]) -> Any:
    input_list.reverse()
    return input_list


def contains(input_list: List[Any], element: Any) -> bool:
    return element in input_list


def odd_elements(input_list: List[Any]) -> List[Any]:
    return input_list[::2]


def total(input_list: List[Number]) -> Number:
    return sum(input_list)
