"""
This module implements merge sort using helper functions from the rand module
to generate a random array.
"""

import rand


def merge_sort(array_to_sort):
    """
    Perform a merge sort on the input array.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A sorted list.
    """
    if len(array_to_sort) == 1:
        return array_to_sort

    half = len(array_to_sort) // 2
    return recombine(merge_sort(array_to_sort[:half]), merge_sort(array_to_sort[half:]))

def recombine(left_arr, right_arr):
    """
    Recombine two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left half of the sorted array.
        right_arr (list): The right half of the sorted array.

    Returns:
        list: A merged and sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[right_index + i] = left_arr[i]

    return merge_arr


# Generate a random array using the function from rand module
input_array = rand.random_array([None] * 20)
sorted_array = merge_sort(input_array)


# Print the sorted output array
print(sorted_array)
