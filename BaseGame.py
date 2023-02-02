from tkinter import *

# Create the main window
root = Tk()
root.title("Sudoku")

# Create a 2D array to represent the Sudoku grid
grid = [[0 for x in range(9)] for y in range(9)]

# Populate the grid with some initial values
grid[0][0] = 5
grid[0][4] = 6
grid[1][2] = 3

# Create a function to draw the Sudoku grid on the screen
def draw_grid():
  for i in range(9):
    for j in range(9):
      # Create a text entry for each cell in the grid
      entry = Entry(root, width=2, font=("Helvetica", 20))
      entry.grid(row=i, column=j)

      # If the cell contains a value, set it as the initial value of the text entry
      if grid[i][j] != 0:
        entry.insert(0, str(grid[i][j]))

# Create a function to solve the Sudoku puzzle
# Solve the puzzle here...
# Create a function to solve the Sudoku puzzle using backtracking
def solve():
  # Find the next empty cell in the grid
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        # Try filling in the cell with a number from 1 to 9
        for num in range(1, 10):
          if is_valid(i, j, num):
            # If the number is valid, fill in the cell and recursively try to solve the rest of the puzzle
            grid[i][j] = num
            if solve():
              return True
            # If the puzzle cannot be solved, backtrack and try a different number
            grid[i][j] = 0
        # If no valid number was found, return False to trigger backtracking
        return False
  # If the puzzle is solved, return True
  return True

# Create a function to check if a given number can be placed in a given cell
def is_valid(row, col, num):
  # Check if the number is already present in the given row
  if num in grid[row]:
    return False

  # Check if the number is already present in the given column
  for i in range(9):
    if grid[i][col] == num:
      return False

  # Check if the number is already present in the 3x3 subgrid
  start_row = row // 3 * 3
  start_col = col // 3 * 3
  for i in range(3):
    for j in range(3):
      if grid[start_row + i][start_col + j] == num:
        return False

  # If the number is not present in the row, column, or subgrid, it is valid
  return True

  # For example, you could use a backtracking algorithm to fill in the grid with the solution
  pass

# Call the draw_grid function to draw the initial Sudoku grid
draw_grid()

# Create a "Solve" button to solve the puzzle
solve_button = Button(root, text="Solve", padx=10, pady=10, command=solve)
solve_button.grid(row=9, column=10)

# Fix grid spacing to create 3x3 gird of 3x3 grids

# Start the main event loop
root.mainloop()
