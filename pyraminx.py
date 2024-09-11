class sticker:
    def __init__(self, position: int, color: str) -> None:
        self.position = position
        self.color = color
        self.previous = []


class Pyraminx:
    def __init__(self) -> None:
        self.red_face = []
        self.blue_face = []
        self.green_face = []
        self.yellow_face = []

        self.initialize()

        self.faces = [self.red_face,
                      self.blue_face,
                      self.green_face,
                      self.yellow_face]

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

    def color_matching(self, row_num):
        row_colors = []
        for face in self.faces:
            row = face[row_num]
            for sticker in row:
                row_colors.append(sticker.color)

        matching_letters = []
        for color in row_colors:
            if color == "red":
                matching_letters.append("R")
            if color == "blue":
                matching_letters.append("B")
            if color == "yellow":
                matching_letters.append("Y")
            if color == "green":
                matching_letters.append("G")
        
        return matching_letters

    def determine_spaces(self, row_num):
        starting_space_count = {
            1 : [6, 14],
            2 : [4, 10],
            3 : [2, 6],
            4 : [0, 2]
        }
        
        return starting_space_count[row_num]


    def print_pyraminx(self):
        # for row #1
        matching_letters_1 = self.color_matching(0)
        space_count_1 = self.determine_spaces(1)
        first_row_str = " " * space_count_1[0]
        for letter in matching_letters_1:
            first_row_str += letter
            first_row_str += " " * space_count_1[1]
        
        print(first_row_str)

        # second row
        matching_letters_2 = self.color_matching(1)
        space_count_2 = self.determine_spaces(2)
        second_row_str = " " * space_count_2[0]
        i = 1
        for letter in matching_letters_2:
            second_row_str += letter

            if i % 3 == 0:
                second_row_str += " " * space_count_2[1]
            else: 
                second_row_str += " "

            i += 1

        print(second_row_str)

        # third row 
        matching_letters_3 = self.color_matching(2)
        space_count_3 = self.determine_spaces(3)
        third_row_str = " " * space_count_3[0]

        i = 1
        for letter in matching_letters_3:
            third_row_str += letter

            if i % 5 == 0:
                third_row_str += " " * space_count_3[1]
            else:
                third_row_str += " "

            i += 1

        print(third_row_str)

        # third row 
        matching_letters_4 = self.color_matching(3)
        space_count_4 = self.determine_spaces(4)
        fourth_row_str = " " * space_count_4[0]

        i = 1
        for letter in matching_letters_4:
            fourth_row_str += letter

            if i % 7 == 0:
                fourth_row_str += " " * space_count_4[1]
            else:
                fourth_row_str += " "

            i += 1

        print(fourth_row_str)