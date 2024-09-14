class sticker:
    def __init__(self, position: int, color: str) -> None:
        self.position = position
        self.color = color
        # self.previous = []


class Pyraminx:
    def __init__(self) -> None:
        self.red_face = []
        self.blue_face = []
        self.green_face = []
        self.yellow_face = []

        self.yellow_face_left = []

        self.initialize()

        self.faces = [self.red_face,
                      self.blue_face,
                      self.green_face,
                      self.yellow_face]

    def create_corresponding_yellow(self):
        row_one = []
        row_two = []
        row_three = []
        row_four = []

        row_one.append(self.yellow_face[3][6])
        row_two.append(self.yellow_face[3][4])
        row_two.append(self.yellow_face[3][5])
        row_two.append(self.yellow_face[2][4])

    def match_hor_and_dia(self, row):
        self.yellow_face[3][6] = row[0]
        self.yellow_face[3][6] = self.yellow_face_left[0][0]
        self.yellow_face[3][4] = self.yellow_face_left[1][0]

    def create_faces(self, face_color: str) -> list[list]:
        """
        Given the face color, return the array that stores all stickers of that face
        """
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
        """
        Helper function for print: Given a row number, return the corresponsing color letter for that row in all faces
        """
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
        """
        Helper function for print: Given a row number, return a list that has the number of spaces needed for printing.
        """
        starting_space_count = {
            1 : [6, 14],
            2 : [4, 10],
            3 : [2, 6],
            4 : [0, 2]
        }
        
        return starting_space_count[row_num]

    def print_pyraminx(self):
        """
        Prints the current state of the pyraminx. 
        """
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

    def rearrange_green(self, is_clockwise: bool) -> None:
        """
        Rearranges the green side when the 4th row of front face is rotated. 
        """
        if is_clockwise:
            temp_tip = self.green_face[0][0]
            temp_11 = self.green_face[1][1]
            temp_12 = self.green_face[1][2]
            temp_23 = self.green_face[2][3]
            temp_24 = self.green_face[2][4]

            self.green_face[0][0] = self.green_face[3][6]
            self.green_face[1][1] = self.green_face[3][5]
            self.green_face[1][2] = self.green_face[3][4]
            self.green_face[2][3] = self.green_face[3][3]
            self.green_face[2][4] = self.green_face[3][2]
            self.green_face[3][5] = self.green_face[3][1]
            self.green_face[3][6] = self.green_face[3][0] 

            temp_10 = self.green_face[1][0]
            temp_21 = self.green_face[2][1]
            temp_20 = self.green_face[2][0]

            self.green_face[3][0] = temp_tip
            self.green_face[3][1] = temp_11
            self.green_face[2][0] = temp_12
            self.green_face[2][1] = temp_23
            self.green_face[1][0] = temp_24

            self.green_face[3][2] = temp_10
            self.green_face[3][3] = temp_21
            self.green_face[3][4] = temp_20
        else:
            temp_11 = self.green_face[1][1]
            temp_00 = self.green_face[0][0]
            temp_24 = self.green_face[2][4]
            temp_23 = self.green_face[2][3]
            temp_12 = self.green_face[1][2]

            self.green_face[0][0] = self.green_face[3][0]
            self.green_face[1][1] = self.green_face[3][1]
            self.green_face[1][2] = self.green_face[2][0]
            self.green_face[2][3] = self.green_face[2][1]
            self.green_face[2][4] = self.green_face[1][0]
            self.green_face[3][5] = temp_11
            self.green_face[3][6] = temp_00

            self.green_face[1][0] = self.green_face[3][2]
            self.green_face[2][1] = self.green_face[3][3]
            self.green_face[2][0] = self.green_face[3][4]
            self.green_face[3][1] = self.green_face[3][5]
            self.green_face[3][0] = self.green_face[3][6]

            self.green_face[3][2] = temp_24
            self.green_face[3][3] = temp_23
            self.green_face[3][4] = temp_12

    def rotate_front_rows(self, is_clockwise: bool, row_num: int) -> None:
        """
        Rotate a row of the front face(which is red) given the direction and row number
        """
        if is_clockwise:
            temp_row = self.red_face[row_num-1]
            self.red_face[row_num-1] = self.blue_face[row_num-1]
            self.blue_face[row_num-1] = self.yellow_face[row_num-1]
            self.yellow_face[row_num-1] = temp_row
        else:
            temp_row = self.red_face[row_num-1]
            self.red_face[row_num-1] = self.yellow_face[row_num-1]
            self.yellow_face[row_num-1] = self.blue_face[row_num-1]
            self.blue_face[row_num-1] = temp_row

        if row_num == 4:
            self.rearrange_green(is_clockwise)

    def rotate_left_rows(self, is_clockwise: bool, row_num: int) -> None:
        for front_sticker, left_sticker, right_sticker in zip(self.red_face_left[row_num-1], self.blue_face_left[row_num-1]):
            if is_clockwise:
                temp_sticker_1 = self.green_face[3][6]
                temp_sticker_2 = self.yellow_face[3][6]
                self.yellow_face[3][6] = temp_sticker_1
                self.green_face[3][6] = self.red_face[3][0]
                self.red_face[3][0] = temp_sticker_2

