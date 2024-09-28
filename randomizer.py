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
    for _ in range(num_moves):
        movePicker(pyraminx)
    return pyraminx

def movePicker(pyraminx):
    """
    Function that randomly selects a move and applies it to the Pyraminx.
    Moves include front face row rotation or diagonal layer rotation.
    
    Args:
        pyraminx: The Pyraminx puzzle object.
    """
    move_type = random.choice(["front_row", "diagonal"])
    layer_or_row = random.randint(1, 4)  # Randomly choose a row or layer (1 to 4)
    diagonal = random.randint(1, 3)  # Randomly choose a diagonal (1 to 3)

    if move_type == "front_row":
        pyraminx.rotate_front_rows(True, layer_or_row)  # Clockwise only
    elif move_type == "diagonal":
        pyraminx.rotate_diagonal_layer(diagonal, True, layer_or_row)  # Clockwise only
