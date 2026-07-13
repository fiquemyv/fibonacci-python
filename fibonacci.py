def fibonacci(length: int) -> list[int]:
    """
    Generate a Fibonacci sequence of a given length.

    Args:
        length (int): Number of Fibonacci numbers to generate.

    Returns:
        list[int]: Fibonacci sequence.

    Raises:
        ValueError: If length is negative.
        TypeError: If length is not an integer.

    """

    if not isinstance(length, int):
        raise TypeError("Length must be an integer")

    if length < 0:
        raise ValueError("Length cannot be negative")

    if length == 0:
        return []

    if length == 1:
        return [0]

    numbers = [0, 1]

    while len(numbers) < length:
        numbers.append(numbers[-1] + numbers[-2])

    return numbers


print(fibonacci(10))