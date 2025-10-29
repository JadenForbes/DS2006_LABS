def add_list(numbers: list[float]) -> int:
    """Return the sum of all numbers in the list."""
    return int(sum(numbers))


def subtract_list(numbers: list[float]) -> int:
    """
    Subtract all subsequent numbers from the first element in the list.
    Example: [20, 10, 5] → 20 - 10 - 5 = 5
    """
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return int(result)


def multiply_list(numbers: list[float]) -> int:
    """Multiply all numbers in the list and return the result."""
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return int(result)


def divide_list(numbers: list[float]) -> list[float]:
    """
    Divide all numbers in the list by 2 and return a new list.
    Example: [4, 8] → [2.0, 4.0]
    """
    return [num / 2 for num in numbers]
