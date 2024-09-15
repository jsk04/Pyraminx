class sticker:
    def __init__(self, position: int, color: str) -> None:
        self.position = position
        self.color = color
        # self.previous = [] #Placeholder for heuristic


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

    def rotate_diagonal_layer(self, diagonal: int, is_clockwise: bool, layer: int) -> None:
        """
        Rotates the given diagonal for a specific layer using the green face tips as reference.
        Handles the diagonal transformation for red, yellow, blue, and green faces.
        
        '1' -> Affects diagonal from top-left to bottom-right (left tip of green as reference).
        '2' -> Affects diagonal from top-right to bottom-left (right tip of green as reference).
        '3' -> Affects diagonal from bottom-left to top-right (bottom tip of green as reference).
           
        Based on print view:
                       G  <- 1 (rotates red,yellow,green)
                      GGG
                     GGGGG
               3 -> GGGGGGG <- 2 (rotates red, blue, green)
        
        The 'layer' parameter specifies which layer (1 to 4) to rotate.
        """
        
        if layer < 1 or layer > 4:
            raise ValueError("Layer must be between 1 and 4")

        # Predefined index mappings for the faces based on diagonal and layer
        if diagonal == 1:
            # Diagonal from top-left to bottom-right, using the left tip of the green face as reference
            if layer == 1:
                face1_indices  = [(3, 0)]     # Red bottom-left
                face2_indices  = [(3, 6)]  # Yellow bottom-right
                green_indices = [(3, 0)]   # Green top-left (left tip)
                face1 = self.red_face
                face2 = self.yellow_face
            elif layer == 2:
                face1_indices  = [(2, 0), (3, 1), (3, 2)]     # Second row of red
                face2_indices  = [(2, 4), (3, 4), (3, 5)]  # Second row of yellow
                green_indices = [(1, 0), (1, 1), (1, 2)]   # Second row of green
                face1 = self.red_face
                face2 = self.yellow_face
            elif layer == 3:
                face1_indices = [(1, 0), (2, 1), (2, 2), (3, 3), (3, 4)]     # Third row of red
                face2_indices = [(1, 2), (2, 2), (2, 3), (3, 2), (3, 3)]  # Third row of yellow
                green_indices = [(2, 0), (2, 1), (2, 2), (2,3), (2, 4)]   # Third row of green
                face1 = self.red_face
                face2 = self.yellow_face
            elif layer == 4:
                face1_indices = [(0, 0), (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6)]  # Fourth row of red
                face2_indices = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]  # Fourth row of yellow
                green_indices = [(3, 0), (3, 1), (3, 2), (3,3), (3, 4), (3, 5), (3, 6)]   # Fourth row of green
                face1 = self.red_face
                face2 = self.yellow_face

        elif diagonal == 2:
            # Diagonal from top-right to bottom-left, using the right tip of the green face as reference
            if layer == 1:
                face1_indices = [(3, 0)]    # Blue bottom-left
                face2_indices = [(3, 6)]     # Red bottom-right
                green_indices = [(3, 6)]   # Green top-right (right tip)
                face1 = self.blue_face
                face2 = self.red_face
            elif layer == 2:
                face1_indices = [(2, 0), (3, 1), (3, 2)]    # Second row of blue
                face2_indices = [(2, 4), (3, 4), (3, 5)]     # Second row of red
                green_indices = [(2, 4), (3, 4),(3, 5)]   # Second row of green (correcting indices)
                face1 = self.blue_face
                face2 = self.red_face
            elif layer == 3:
                face1_indices = [(1, 0), (2, 1), (2, 2), (3, 3), (3, 4)]    # Third row of blue
                face2_indices = [(1, 2), (2, 2), (2, 3), (3, 2), (3, 3)]     # Third row of red
                green_indices = [(1, 2), (2, 2), (2, 3), (3, 2), (3, 3)]   # Third row of green (corrected)
                face1 = self.blue_face
                face2 = self.red_face
            elif layer == 4:
                face1_indices = [(0, 0), (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6)]  # Fourth row of blue
                face2_indices = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]  # Fourth row of red
                green_indices = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]  # Fourth row of green
                face1 = self.blue_face
                face2 = self.red_face

        elif diagonal == 3:
            # Diagonal from bottom-left to top-right, using the bottom-left tip of the green face as reference
            if layer == 1:
                face1_indices = [(3, 0)]  # Yellow bottom-left
                face2_indices = [(0, 0)]    # Blue bottom-right
                green_indices = [(3, 0)]   # Green bottom-left (bottom tip)
                face1 = self.yellow_face
                face2 = self.blue_face
            elif layer == 2:
                face1_indices = [(2, 0), (3, 1), (3, 2)]  # Second row of yellow
                face2_indices = [(2, 4), (3, 4), (3, 5)]    # Second row of blue
                green_indices = [(2, 0), (3, 1), (3, 2)]   # Second row of green
                face1 = self.yellow_face
                face2 = self.blue_face
            elif layer == 3:
                face1_indices = [(1, 0), (2, 1), (2, 2), (3, 3), (3, 4)]  # Third row of yellow
                face2_indices = [(1, 2), (2, 2), (2, 3), (3, 2), (3, 3)]    # Third row of blue
                green_indices = [(1, 0), (2, 1), (2, 2), (3, 3), (3, 4)]   # Third row of green
                face1 = self.yellow_face
                face2 = self.blue_face
            elif layer == 4:
                face1_indices = [(0, 0), (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6)]  # Fourth row of yellow
                face2_indices = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]    # Fourth row of blue
                green_indices = [(0, 0), (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6)]   # Fourth row of green
                face1 = self.yellow_face
                face2 = self.blue_face
        
        # Apply the rotation for the selected layer
        self._rotate_face_elements(face1, face2, self.green_face, face1_indices, face2_indices, green_indices, is_clockwise)

    def _rotate_face_elements(self, face1, face2, green_face, face1_indices, face2_indices, green_indices, is_clockwise):
        """
        Rotates the elements of three faces (face1, face2, green) based on the given indices.
        Uses clockwise or counterclockwise rotation.
        """
        if is_clockwise:
            # Temporarily store the face1 values
            temp = [face1[r][c] for r, c in face1_indices]

            # Perform clockwise shift
            for i in range(len(face1_indices)): #i is the picition of layers in the indice being passed
                face1[face1_indices[i][0]][face1_indices[i][1]] = \
                    face2[face2_indices[i][0]][face2_indices[i][1]]
                face2[face2_indices[i][0]][face2_indices[i][1]] = \
                    green_face[green_indices[i][0]][green_indices[i][1]]
                green_face[green_indices[i][0]][green_indices[i][1]] = temp[i]
        else:
            # Temporarily store the green_face values
            temp = [green_face[r][c] for r, c in green_indices]

            # Perform counterclockwise shift
            for i in range(len(face1_indices)):
                green_face[green_indices[i][0]][green_indices[i][1]] = \
                    face2[face2_indices[i][0]][face2_indices[i][1]]
                face2[face2_indices[i][0]][face2_indices[i][1]] = \
                    face1[face1_indices[i][0]][face1_indices[i][1]]
                face1[face1_indices[i][0]][face1_indices[i][1]] = temp[i]
