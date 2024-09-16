from pyraminx import Pyraminx
from randomizer import randomizer

def main():
    pyraminx = Pyraminx()
    
    print("Welcome to the Pyramix Simulator!")
    print("You can simulate the puzzle by performing different types of rotations.")
    print("Our puzzle does rotations using the red face as reference, here is a diagram of how the faces are located relative to each other:")
    print("Unfolded view of pyramix:\nY R B\n  G")    
    # Game Mode Selection
    game_mode = int(input("Choose game mode:\n1. Free (Start with an unscrambled cube)\n2. Random (Start with a scrambled cube)\n"))
    
    if game_mode == 2:
        num_moves = int(input("How many moves do you want to scramble the cube with? "))
        randomizer(num_moves, pyraminx)
        print("\nYour cube has been scrambled with", num_moves, "random moves.\n")
    
    pyraminx.print_pyraminx()  # Display the cube
    
    while True:
        # Choose the type of rotation
        move_type = int(input("\nChoose the type of rotation you want:\n1. Horizontal Rotation\n2. Diagonal Rotation\n3. Quit\n"))
        
        if move_type == 3:
            print("Exiting the Pyramix Simulator. Goodbye!")
            break
        
        if move_type == 1:
            # Horizontal Rotation
            layer = int(input("\nChoose the layer you want to rotate:\n1. Tip/First layer\n2. Second layer\n3. Third layer\n4. Fourth layer\n"))
            direction = int(input("\nChoose rotation direction:\n1. Clockwise\n2. Counterclockwise\n"))
            is_clockwise = True if direction == 1 else False
            pyraminx.rotate_front_rows(is_clockwise, layer)
        
        elif move_type == 2:
            # Diagonal Rotation
            diagonal = int(input("\nChoose the diagonal move:\n1. Tip in lower left corner of red face\n2. Tip in lower right corner of red face\n3. Lower tip between yellow and blue\n"))
            layer = int(input("\nChoose the layer you want to rotate:\n1. Tip/First layer\n2. Second layer\n3. Third layer\n4. Fourth layer\n"))
            direction = int(input("\nChoose rotation direction:\n1. Clockwise\n2. Counterclockwise\n"))
            is_clockwise = True if direction == 1 else False
            pyraminx.rotate_diagonal_layer(diagonal, is_clockwise, layer)
        
        # Display the updated cube after each move
        pyraminx.print_pyraminx()

if __name__ == "__main__":
    main()