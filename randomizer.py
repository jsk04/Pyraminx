from pyraminx import Pyraminx
import random


"""
Funtion:
            randomizer(numMoves:  int)
Description:
            Function that takes integer numMoves as input to carry out number of randomized pyramix cube moves equal to numMoves.
Arguments:
            numMoves: Integer that especifies desired number of moves to scramble the pyramix. 
"""

def randomizer(numMoves: int, pyraminx):
    for x in range(numMoves):
        pyraminx = movePicker(pyraminx)

    return pyraminx
    

"""
Funtion:
            movePicker():
Description:
            Function that calls a random move for the pyramix.
"""
def movePicker(pyraminx):
    move = random.randrange(4)

    match move:
        case 0:
            pyraminx.rotate_front_tip(False)
        case 1:
            pyraminx.rotate_front_two(False)
        case 2:
            pyraminx.rotate_front_tip(True)
        case 3:
            pyraminx.rotate_front_two(True)

    return pyraminx