class Sticker:
    def __init__(self, color):
        self.color = color
        self.history = []

    def move(self, new_position):
        self.history.append(new_position)

    def current_position(self):
        return self.history[-1] if self.history else None


class Face:
    def __init__(self, color):
        # We represent the face as a list of lists, corresponding to each layer
        # There are 4 layers: 1 sticker, 3 stickers, 5 stickers, and 7 stickers
        self.color = color
        self.layers = [
            [Sticker(color)] * 1,  # 1st layer
            [Sticker(color)] * 3,  # 2nd layer
            [Sticker(color)] * 5,  # 3rd layer
            [Sticker(color)] * 7   # 4th layer
        ]

    def get_layers(self):
        return [[sticker.color for sticker in layer] for layer in self.layers]


class Pyramix:
    def __init__(self):
        # Initialize the Pyramix with four faces
        self.faces = {
            'Red': Face('R'),
            'Blue': Face('B'),
            'Yellow': Face('Y'),
            'Green': Face('G')
        }

    def display_unfolded(self):
        # Get layers from each face
        yellow_layers = self.faces['Yellow'].get_layers()
        red_layers = self.faces['Red'].get_layers()
        blue_layers = self.faces['Blue'].get_layers()
        green_layers = self.faces['Green'].get_layers()

        # Unfolded display with specific alignment
        # Align the Yellow, Red, Blue, and Green faces in the desired format
        print(f"     {' '.join(yellow_layers[0])}              {' '.join(red_layers[0])}              {' '.join(blue_layers[0])}")
        print(f"   {' '.join(yellow_layers[1])}          {' '.join(red_layers[1])}          {' '.join(blue_layers[1])}")
        print(f"  {' '.join(yellow_layers[2])}     {' '.join(red_layers[2])}     {' '.join(blue_layers[2])}")
        print(f"{' '.join(yellow_layers[3])} {' '.join(red_layers[3])} {' '.join(blue_layers[3])}")
        print(f"              {' '.join(green_layers[3])}")
        print(f"                 {' '.join(green_layers[2])}")
        print(f"                   {' '.join(green_layers[1])}")
        print(f"                     {' '.join(green_layers[0])}")

    def scramble(self, moves):
        # Functionality to perform scrambling with a defined number of moves
        pass

    def is_solved(self):
        # Check if the Pyramix is solved
        for face in self.faces.values():
            for layer in face.layers:
                if not all(sticker.color == face.color for sticker in layer):
                    return False
        return True


# Example usage
puzzle = Pyramix()
puzzle.display_unfolded()

print("\nIs the puzzle solved?", puzzle.is_solved())
