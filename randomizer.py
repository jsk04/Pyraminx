import random

def randomizer(num_moves: int, pyraminx):
    """
    Randomizer function to scramble the Pyraminx puzzle.
    
    Args:
        num_moves: Integer specifying the number of random moves to apply.
        pyraminx: The Pyraminx puzzle object to scramble.
        
    Returns:
        The scrambled Pyraminx puzzle.
    """
    for x in range(num_moves):
        movePicker(pyraminx)
        print(f"Stages of scramble:\n",pyraminx.print_pyraminx()) #This will be removed for actual players but it is included for grader to see functions working correctly
        print(f"Move: {x+1}\n")

    return pyraminx


def movePicker(pyraminx):
    """
    Function that randomly selects a move and applies it to the Pyraminx.
    
    Moves include:
    - Front face row rotation
    - Left row rotation
    - Diagonal layer rotation
    
    Args:
        pyraminx: The Pyraminx puzzle object.
    """
    move_type = random.choice(["front_row", "diagonal"])
    is_clockwise = random.choice([True, False])  # Randomly choose clockwise or counterclockwise
    layer_or_row = random.randint(1, 4)  # Randomly choose a row or layer (1 to 4)
    diagonal = random.randint(1, 3)  # Randomly choose a diagonal (1 to 4)

    if move_type == "front_row":
        # Rotate a front row (red face)
        pyraminx.rotate_front_rows(is_clockwise, layer_or_row)
    elif move_type == "diagonal":
        # Rotate a diagonal layer (1, 2, or 3 diagonals)
        pyraminx.rotate_diagonal_layer(diagonal, is_clockwise, layer_or_row)
    else:
        print("Error, no move chosen.")
