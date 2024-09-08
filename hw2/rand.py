"""
This module provides a utility function to generate a random array of integers
using the 'shuf' command from the subprocess module.
""" 


import subprocess


def random_array(arr):
    """
    Generate a random array by shuffling numbers.

    Args:
        arr (list): A list initialized with None values.

    Returns:
        list: A list filled with randomly generated numbers.
    """
    for index, _ in enumerate(arr):
        try:
            # Use subprocess to generate a random number between 1 and 20
            shuffled_num = subprocess.run(
                ["shuf", "-i1-20", "-n1"], capture_output=True, text=True, check=True
            )
            # Convert the output to an integer and assign it to the current position
            arr[index] = int(shuffled_num.stdout.strip())
        except (subprocess.CalledProcessError, ValueError):
            print(f"Error generating random number for index {index}.")
            arr[index] = 0  # Assign a default value or handle the error as needed
    return arr
