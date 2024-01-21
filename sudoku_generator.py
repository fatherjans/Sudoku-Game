import math,random
from random import randint
"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = 9
        self.removed_cells = removed_cells
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.box_length = 3
    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    # function that returns 9x9 list
    def get_board(self):
        return self.board
    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    # function to print board
    def print_board(self):
        # for loop to print list, one row in one line, then move down line for next row
        for r in range(0, len(self.board)):
            for c in range(0, len(self.board[r])):
                print(self.board[r][c], end=' ')
                print('')

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    # function to check if number is in specific row
    def valid_in_row(self, row, num):
        # for loop to check each number in row
        for each_col in range(0, 9):
            # if it equals each other, return false
            if self.get_board()[row][each_col] == num:
                return False
        # if none of them match, return true
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    # function to check if number is in specific column
    def valid_in_col(self, col, num):
        # for loop to check rows
        for each_row in range(0, 9):
            # they equal, return false
            if self.get_board()[each_row][col] == num:
                return False
        # if none of them match, return true
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    # function to check each cell in 3x3 box with starting points
    def valid_in_box(self, row_start, col_start, num):
        # trying 9 different row column combinations to check number, and if it is return false
        if self.get_board()[row_start][col_start] == num:
            return False
        elif self.get_board()[row_start + 1][col_start] == num:
            return False
        elif self.get_board()[row_start + 2][col_start] == num:
            return False
        elif self.get_board()[row_start][col_start + 1] == num:
            return False
        elif self.get_board()[row_start + 1][col_start + 1] == num:
            return False
        elif self.get_board()[row_start + 2][col_start + 1] == num:
            return False
        elif self.get_board()[row_start][col_start + 2] == num:
            return False
        elif self.get_board()[row_start + 1][col_start + 2] == num:
            return False
        elif self.get_board()[row_start + 2][col_start + 2] == num:
            return False
        # if number not in any of 9 cells, return true
        else:
            return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    # function to check if able to enter number based on row, column, and box
    def is_valid(self, row, col, num):
        # check row number and assign start row for box
        if row <= 2:
            start_row = 0
        elif row > 2 and row <= 5:
            start_row = 3
        elif row > 5 and row <= 8:
            start_row = 6
        # check col number and assign start col for box
        if col <= 2:
            start_col = 0
        elif col > 2 and col <= 5:
            start_col = 3
        elif col > 5 and col <= 8:
            start_col = 6
        # if functions for row, col, or box return false, make function return false
        if self.valid_in_row(row, num) == False:
            return False
        elif self.valid_in_col(col, num) == False:
            return False
        elif self.valid_in_box(start_row, start_col, num) == False:
            return False
        # if they all return false, return true
        else:
            return True


    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    # function to fill box without repeating numbers
    def fill_box(self, row_start, col_start):
        # iterate 9 times for 9 cells
        for i in range(0, 9):
            # generate random number between 1 and 9
            random_num = randint(1, 9)
            # first iteration start with original point
            if i == 0:
                row = row_start
                col = col_start
            # 2, 3 iterations increase row by 1
            elif i == 1:
                row = row_start + 1
                col = col_start
            elif i == 2:
                row = row_start + 2
                col = col_start
            # 4, 5, 6 iterations increase col by 1 and row 0, 1, 2
            elif i == 3:
                row = row_start
                col = col_start + 1
            elif i == 4:
                row = row_start + 1
                col = col_start + 1
            elif i == 5:
                row = row_start + 2
                col = col_start + 1
            # 4, 5, 6 iterations increase col by 2 and row 0, 1, 2
            elif i == 6:
                row = row_start
                col = col_start + 2
            elif i == 7:
                row = row_start + 1
                col = col_start + 2
            elif i == 8:
                row = row_start + 2
                col = col_start + 2
            # create condition and while loop
            valid_num = False
            while valid_num == False:
                # if not valid in row column and box, generate another number until valid
                if self.is_valid(row, col, random_num) == False:
                    random_num = randint(1, 9)
                else:
                    valid_num = True
                    break
            # insert valid value in cell
            self.get_board()[row][col] = random_num
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    # function to fill boxes that are diagonal
    def fill_diagonal(self):
        # fill boxes at (0, 0), (3, 3), (6, 6)
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    # function to remove random cells
    def remove_cells(self):
        # for loop to the number of times as removed cells
        for i in range(0, self.removed_cells):
            # generate random row and col
            random_row = randint(0, 8)
            random_col = randint(0, 8)
            # create while loop condition until it reaches cell that is not already 0
            valid_cell = False
            while valid_cell == False:
                # if cell is already 0, then generate new random row and col
                if self.get_board()[random_row][random_col] == 0:
                    random_row = randint(0, 8)
                    random_col = randint(0, 8)
                # if it is valid break loop
                else:
                    valid_cell = True
                    break
            # change specific row and col to 0
            self.get_board()[random_row][random_col] = 0
    def find_empty(self):
        # variables row and col
        row = 0
        col = 0
        # range of 81 cells
        for i in range(0, 81):
            # if cell is empty return location
            if self.get_board()[row][col] == 0:
                return (row, col)
            # else, increase row until end, then reset row and increase col
            else:
                if row < 8:
                    row += 1
                elif row >= 8:
                    row = 0
                    col += 1
        return None
    def check_board(self, save_for_sol):
        # variables row and col
        row = 0
        col = 0
        # range of 81 cells
        for i in range(0, 81):
            # if cell value isn't valid, return false
            if save_for_sol[row][col] != self.board[row][col]:
                return False
            # else, increase row until end, then reset row and increase col
            else:
                if row < 8:
                    row += 1
                elif row >= 8:
                    row = 0
                    col += 1
        # if all 81 cell values are valid
        return True
'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board