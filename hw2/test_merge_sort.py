"""
This module contains functions for merge sort.
"""
from random import randint

from hw2_debugging import merge_sort

# Test case 1: Sorting a list of random integers


def test_random_integers():
    """
    Test merge_sort method with random integers
    """
    input_list = [randint(1, 100) for _ in range(10)]
    sorted_list = sorted(input_list)
    assert merge_sort(input_list) == sorted_list

# Test case 2: Sorting an already sorted list


def test_sorted_list():
    """
    Test merge_sort method with sorted list
    """
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert merge_sort(input_list) == input_list

# Test case 3: Sorting a list with duplicate values


def test_list_with_duplicates():
    """
    Test merge_sort method with duplicates
    """
    input_list = [5, 3, 8, 3, 5, 1, 7]
    sorted_list = [1, 3, 3, 5, 5, 7, 8]
    assert merge_sort(input_list) == sorted_list
