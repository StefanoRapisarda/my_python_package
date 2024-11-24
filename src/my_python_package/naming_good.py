def multiply_by_sum(number, values):
    """Multiplies a number by the sum of a list of values."""
    total = 0
    for value in values:
        total += value
    return number * total


multiplier = 5
numbers = [1, 2, 3]

result = multiply_by_sum(multiplier, numbers)

print(result)
