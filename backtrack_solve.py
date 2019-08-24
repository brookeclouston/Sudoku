"""
Author: Brooke Clouston
Date Created: August 24 2019
This script uses a backtracking algorithim to recursively solve a randomly generated sudoku board.
"""
from build_graph import Graph

class SudokuSolver:
    """ Class: SudokuSolver
    Solves a generated sudoku game using backtracking. """

    def __init__(self):
        """ Function: __init__
        Initalizes attribites, controls flow of executing, displays boards. """
        while True:
            self.graph = Graph()
            self.board = self.graph.build_table()
            print("Starting board:")
            self.graph.display()
            self.solve()
            if self.get_empty():
                print("\nUnable to solve, generating new board")
            else:
                break
        print("Completed board:")
        self.graph.display()

    def solve(self):
        """ Function: solve
        Uses backtracking to solve the puzzle by recusively checking for valid entries until
        the board has been completed or no valid solution is found. """
        pos = self.get_empty()
        if not pos:
            return True
        row, col = pos
        for num in range(1, 10):
            if self.graph.validate(num, row, col):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "x"
        return False

    def get_empty(self):
        """ Function: get_empty
        Returns the next unfilled space in the board or False if the board is complete. """
        for row in range(0, 9):
            for col in range(0, 9):
                num = self.board[row][col]
                if num == "x":
                    return (row, col)
        return False

if __name__ == "__main__":
    SudokuSolver()
