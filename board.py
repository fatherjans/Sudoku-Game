from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
from cell import Cell
import pygame


class Board:
    def __init__(self, width, height, screen, difficulty):
        # Initialize the board's size and difficulty level
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        # Drawing horizontal and vertical lines for cells
        for i in range(0, 10):
            pygame.draw.line(self.screen, (245, 152, 66), (0, i * 75), (self.width, i * 75), 8)
        for i in range(0,10):
            pygame.draw.line(self.screen, (245, 152, 66), (i * 75, 0), (i * 75, self.height), 8)
        for i in range(0, 10, 3):
            pygame.draw.line(self.screen, (245, 152, 66), (0, i * 75), (self.width, i * 75), 14)
        for i in range(0,10, 3):
            pygame.draw.line(self.screen, (245, 152, 66), (i * 75, 0), (i * 75, self.height), 14)

    def select(self, row, col):
        # Select a cell at the specified row and column
        current_selected_cell = SudokuGenerator.get_board()[row][col]

    def click(self, x, y):
        # Convert screen coordinates to row and column indices
        row = y // 75
        col = x // 75
        return (row, col)
    
    def clear(self):
        # Clear the entire board
        for i in range(9):
            for j in range(9):
                self.value == 0

    def place_number(self, value):
        # Place a number on the current cell
        Cell.value = value

    def reset_to_original(self):
        # Reset the board to its original state
        for row in range(9):
            for col in range(9):
                if (row, col) in self.unused_cells:
                    self.cells[row][col].set_cell_value(0)
                    self.cells[row][col].set_sketched_value(0)
                    self.cells[row][col].clicked = False

    def is_full(self):
        # Check if the board is full
        row = 0
        col = 0
        for i in range(0, 81):
            # If cell is empty, return false
            if SudokuGenerator.get_board[row][col] == 0:
                return False
            # Else, increase row until end, then reset row and increase col
            else:
                if row < 8:
                    row += 1
                elif row >= 8:
                    row = 0
                    col += 1
        # If none of cells equal 0, then return true
        return True
    
    def update_board(self):
        # Update the internal representation of the board based on cell values
        for row in range(9):
            for col in range(9):
                self.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        # Find the first empty spot on the board and return its location
        row = 0
        col = 0
        # Range of 81 cells
        for i in range(0, 81):
            # If cell is empty return location
            SG1 = SudokuGenerator(9, 30)
            if SG1.get_board()[row][col] == 0:
                return (row, col)
            # Else, increase row until end, then reset row and increase col
            else:
                if row < 8:
                    row += 1
                elif row >= 8:
                    row = 0
                    col += 1
        return None
    
    def check_board(self):
        # Check if the current state of the board is valid
        row = 0
        col = 0
        # Range of 81 cells
        for i in range(0, 81):
            # If cell value isn't valid, return false
            if SudokuGenerator.is_valid(row, col, SudokuGenerator.get_board()[row][col]) == False:
                return False
            # Else, increase row until end, then reset row and increase col
            else:
                if row < 8:
                    row += 1
                elif row >= 8:
                    row = 0
                    col += 1
        # If all 81 cell values are valid
        return True
