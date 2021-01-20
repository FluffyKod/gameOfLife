#!/usr/bin/env python3

import time
import os
import random
import sys


###################################
# HELPER FUNCTIONS
###################################

def clear_console():
    """
    Clears the console using a system command based on the user's operating system.
    """

    if sys.platform.startswith('win'):
        os.system("cls")
    elif sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('darwin'):
        os.system("clear")


def get_integer_value(prompt, low, high):
    """
    Asks the user for integer input and between given bounds low and high.
    """

    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Input was not a valid integer value.")
            continue
        if value < low or value > high:
            print("Input was not inside the bounds (value <= {0} or value >= {1}).".format(
                low, high))
        else:
            break

    return value


def get_live_neighbors(row, col, rows, cols, grid):
    """
    Counts the number of live cells surrounding a center cell at grid[row][cell]
    """

    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Make sure to count the center cell located at grid[row][col]
            if not (i == 0 and j == 0):
                # Using the modulo operator (%) the grid wraps around
                life_sum += grid[((row + i) % rows)][((col + j) % cols)]

    return life_sum


def print_grid(rows, cols, grid, generation):
    """
    Prints to console the Game of Life grid
    """

    clear_console()

    # A single output string is used to help reduce the flickering caused by printing multiple lines
    output_str = ""

    # Compile the output string together and then print it to console
    output_str += "Generation {0} - To exit the program early press <Ctrl-C>\n\r".format(
        generation)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                output_str += ". "
            else:
                output_str += "@ "
        output_str += "\n\r"
    print(output_str, end=" ")

###################################
# FUNCTIONS TO IMPLEMENT
###################################


def create_initial_grid(rows, cols):
    """
    Creates a random list of lists that contains 1s and 0s to represent the cells in Conway's Game of Life.
    """

    raise NotImplementedError


def create_next_grid(rows, cols, grid, next_grid):
    """
    Analyzes the current generation of the Game of Life grid and determines what cells live and die in the next generation of the Game of Life grid.
    """

    raise NotImplementedError


def grid_changing(rows, cols, grid, next_grid):
    """
    Checks to see if the current generation Game of Life grid differs from the next generation Game of Life grid.
    """

    raise NotImplementedError


def run_game():
    """
    Asks the user for input to setup the Game of Life to run for a given number of generations.
    """

    clear_console()

    # Get the number of rows and columns for the Game of Life grid
    rows = get_integer_value("Enter the number of rows (10-60): ", 10, 60)
    cols = get_integer_value("Enter the number of cols (10-118): ", 10, 118)

    # Get the number of generations that the Game of Life should run for
    generations = get_integer_value(
        "Enter the number of generations (1-100000): ", 1, 100000)

    # Create the initial random Game of Life grids
    current_generation = create_initial_grid(rows, cols)
    next_generation = create_initial_grid(rows, cols)

    # Run Game of Life sequence
    gen = 1
    for gen in range(1, generations + 1):
        if not grid_changing(rows, cols, current_generation, next_generation):
            break

        print_grid(rows, cols, current_generation, gen)
        create_next_grid(rows, cols, current_generation, next_generation)

        # Run automatically
        time.sleep(1 / 5.0)

        # Run manually
        # input()

        current_generation, next_generation = next_generation, current_generation

    print_grid(rows, cols, current_generation, gen)
    input("Press <Enter> to exit.")


# Start the Game of Life
run_game()
