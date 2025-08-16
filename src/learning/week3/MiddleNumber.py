from typing import List


def middle_number(x: int, y: int, z: int) -> int:
    """
    Given three numbers, returns the number which is in the middle
    when the numbers are sorted.
    Args:
        x: First number
        y: Second number
        z: Third number

    Returns:
        int: The number that is neither the biggest nor smallest

    >>> middle_number_efficiency(-10, 10, 5)
    5
    """
    return x + y + z - min(x, y, z) - max(x, y, z)


def middle_number_efficiency(numbers: List[int]) -> int:
    """
    Finds the number that would be in the middle of sequence
    x, y, z, m, and n.
    Precondition:
        No two of x, y, z, m, n are equal.
    Args:
        numbers (List[int]): Input the numbers

    Returns:
        int: The middle number.
    """

    order_numbers = insertion_sort(numbers)
    return order_numbers[len(order_numbers) // 2]




def bubble_sort(nums: List[int]) -> List[int]:
    length = len(nums)
    for _ in range(length):
        for j in range(length - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

def selection_sort(nums: List[int]) -> List[int]:
    """
    Find the smallest number move to the first index of the List array,
    then iterate the List array to order from smallest to biggest
    Args:
        nums: Input a list of numbers

    Returns:
        The list in order

    """
    # <editor-fold desc="Solution 2: Selection Sort">
    length = len(nums)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

    # </editor-fold>

def insertion_sort(nums: List[int]) -> List[int]:
    """
    Start with the first element as sorted,
    take the next element, compare it backward with the sorted part.
    Shift elements to the right until the correct spot is found.
    Insert the element there, continue until all elements are inserted
    Args:
        nums (List[int]): Input a list of numbers.

    Returns:
        a ordered list of number
    """
    # start from the second number
    for i in range(1, len(nums)):
        # key is the current number that want to insert
        key = nums[i]
        # j is initial value (front number)
        j = i - 1
        # j compare with the front number, if j over the current number
        while j >= 0 and nums[j] > key:
            # change their index
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

print(middle_number_efficiency([3, 9, 6, 2, 10]))