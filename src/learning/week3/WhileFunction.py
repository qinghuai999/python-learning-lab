def div_3_5(start: int, end: int) -> int:
    """
    An integer n is divisible by integer m when n % m == 0
        Parameters:
            start (int): Provide a start number
            end (int): Provide a end number
        Returns:
            int: Find the divisible numbers by 3 or 5 between start and end number.
    """
    count = 0
    while start < end:
        if start % 3 == 0 or start % 5 == 0:
            count += 1
        start += 1
    return count

print(div_3_5(0, 1))
