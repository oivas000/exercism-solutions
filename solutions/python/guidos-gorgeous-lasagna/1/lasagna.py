"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# The number of minutes the lasagna is expected to bake in the oven.
EXPECTED_BAKE_TIME = 40

# The number of minutes it takes to prepare a single layer.
PREPARATION_TIME_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of layers you're adding to the lasagna.
    :return: int - total preparation time (in minutes) based on the number of layers.

    This function calculates the preparation time based on a constant time per layer.
    """
    return number_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param number_of_layers: int - the number of layers.
    :param elapsed_bake_time: int - minutes the lasagna has been in the oven.
    :return: int - total time spent so far (in minutes).

    This function returns the total time spent so far, which is the sum of the
    preparation time and the time spent baking.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time

