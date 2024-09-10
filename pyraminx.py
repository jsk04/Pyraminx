class sticker:
    def __init__(self, position: int, colors: list) -> None:
        self.position = position
        self.colors = colors
        self.previous = []


class Pyraminx:
    def __init__(self) -> None:
        self.red_face = []
        self.blue_face = []
        self.green_face = []
        self.yellow_face = []

        self.initialize()

    def create_faces(self, face_color):
        row_one = []
        row_two = []
        row_three = []
        row_four = []

        if face_color == "red":
            start_pos = 1
            end_pos = 17
        elif face_color == "blue":
            start_pos = 17
            end_pos = 33
        elif face_color == "yellow":
            start_pos = 33
            end_pos = 49
        else:
            start_pos = 49
            end_pos = 65

        for pos in range(start_pos, end_pos):
            if(pos == start_pos):
                row_one.append(sticker(1, face_color))  
            if(pos in range(start_pos + 1, start_pos + 4)):
                row_two.append(sticker(pos, face_color))
            if(pos in range(start_pos + 4, start_pos + 9)):
                row_three.append(sticker(pos, face_color))
            if(pos in range(start_pos + 9, end_pos)):
                row_four.append(sticker(pos, face_color))

        return [row_one, row_two, row_three, row_four]
    
    def initialize(self):
        """
        Initialize all faces of pyraminx
        """
    
        self.red_face = self.create_faces("red")
        self.blue_face = self.create_faces("blue")
        self.yellow_face = self.create_faces("yellow")
        self.green_face = self.create_faces("green")

    