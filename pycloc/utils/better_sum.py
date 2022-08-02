from typing import List

def is_int(element) -> bool:
    return isinstance(element, int) or element.isdigit()

def better_sum(random_list: List) -> int:
    """Better version of python sum to summerize array by ignoring any NaN data.

    Args:
        random_list (List): List to sum

    Returns:
        int: Return the sum.
    """
    return sum(int(element) for element in random_list if is_int(element))