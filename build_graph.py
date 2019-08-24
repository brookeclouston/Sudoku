"""
Author: Brooke Clouston
Date Created: August 24 2019
Creates and displays a sudoku board.
"""
import random

class Graph:
    """ Class: Graph
    Creates and displays a sudoku board. """

    def __init__(self):
        """ Function: __init__
        Initializes empty game board. """
        self.board = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],

                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],

                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]

    def build_table(self):
        """ Function: build_table
        Generates a random number of spaces to fill and creates board. """
        spaces_to_fill = random.randint(5, 50)  # this could be config to add difficultly level
        print("SPACES TO FILL:  ", spaces_to_fill)
        while spaces_to_fill > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            element = self.board[row][col]
            if element != "x":
                continue
            num = random.randint(1, 9)
            if not self.validate(num, row, col):
                continue
            self.board[row][col] = num
            spaces_to_fill -= 1
        return self.board

    def validate(self, num, row, col):
        """ Function: validate
        Convience function to validate row, column and squares. """
        if self.check_row(num, row) and \
                self.check_column(num, col) and self.check_square(num, row, col):
            return True
        return False

    def check_row(self, num, row):
        """ Function: check_row
        Validates rows. """
        if num in self.board[row]:
            return False
        return True

    def check_column(self, num, col):
        """ Function: check_column
        Validates columns. """
        for row in self.board:
            if row[col] == num:
                return False
            return True

    def check_square(self, num, row, col):
        """ Function: check_square
        Validates square by separating rows. """
        if row <= 2:
            return self.square_list(col, num, self.board[0], self.board[1], self.board[2])
        if 2 < row <= 5:
            return self.square_list(col, num, self.board[3], self.board[4], self.board[5])
        if row > 5:
            return self.square_list(col, num, self.board[6], self.board[7], self.board[8])

    def square_list(self, col, num, row1, row2, row3):
        """ Function: square_list
        Validates squares by building a list out of columns found in rows. """
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
        """ Function: display
        Displays the current board. """
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
