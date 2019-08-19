""" Builds the initial graph to be used """
import random


class Graph:

    def __init__(self):
        self.board = [["x", "x", "x", "x", "x", "x",  "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],

                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],

                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]

    def get_number(self):
        return random.randint(1, 9)

    def build_table(self):
        """ Builds the table"""
        spaces_to_fill = random.randint(5, 50)  # this could eventually be changed to add in a difficultly level
        print("SPACES TO FILL:  ", spaces_to_fill)
        while spaces_to_fill > 0:
            # this gets a coordinate to fill the board in
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            element = self.board[row][col]
            if element != "x":
                continue
            num = self.get_number()
            if not self.validate(num, row, col):
                continue
            self.board[row][col] = num
            spaces_to_fill -= 1
        self.display()

    def validate(self, num, row, col):
        if self.check_row(num, row) and \
                self.check_column(num, col) and self.check_square(num, row, col):
            return True
        return False

    def check_row(self, num, row):
        """ Validates rows"""
        if num in self.board[row]:
                return False
        return True

    def check_column(self, num, col):
        """ Validates columns"""
        for row in self.board:
            if row[col] == num:
                return False
            return True

    def check_square(self, num, row, col):
        """ Validates square by first separating rows."""
        if row <= 2:
            return self.create_square_list(col, num, self.board[0], self.board[1], self.board[2])
        elif 2 < row <= 5:
            return self.create_square_list(col, num, self.board[3], self.board[4], self.board[5])
        elif row > 5:
            return self.create_square_list(col, num, self.board[6], self.board[7], self.board[8])

    def create_square_list(self, col, num, row1, row2, row3):
        """ Validates squares by building a list out of columns found in rows"""
        if col <= 2:
            square_list = row1[0:3] + row2[0:3] + row3[0:3]
        elif 3 <= col <= 5:
            square_list = row1[3:6] + row2[3:6] + row3[3:6]
        elif col > 5:
            square_list = row1[6:9] + row2[6:9] + row3[6:9]
        if num in square_list:
            return False
        return True

    def display(self):
        """ Displays current board """
        row_count = 0
        for row in self.board:
            col_count = 1
            if row_count in [3, 6]:
                print("\n- - - - - - - - - - -")
            else:
                print()
            row_count += 1
            for element in range(9):
                if col_count in [3, 6]:
                    print(row[element], end=" | ")
                else:
                    print(row[element], end=" ")
                col_count += 1

