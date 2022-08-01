from typing import List


def better_sum(random_list: List) -> int:
    """Better version of python sum to summerize array by ignoring any NaN data.

    Args:
        random_list (List): List to sum

    Returns:
        int: Return the sum.
    """    
    total = 0
    for element in random_list:
        if isinstance(element, int) or element.isdigit():
            total += int(element)

    return total