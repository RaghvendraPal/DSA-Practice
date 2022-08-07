
# minimum island
# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. 
# The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.


# You may assume that the grid contains at least one island.

# minimum island
# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. 
# The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

# You may assume that the grid contains at least one island.

from numpy import Infinity


def minimum_island(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = []
    minSize = Infinity
    # print("First Visit : ",visited)
    for row in range(rows):
        for col in range(cols):
            size = explore(grid, row, col, rows, cols, visited)
            if size and size < minSize:
                minSize = size

    print("minSize : ", minSize)
    return minSize
            


def explore(grid, row, col, rows, cols, visited= None):
    value = str(row)+''+str(col)
    # print(visited)
    if visited is None:
        visited = []

    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0

    if value in visited:
        return 0

    if grid[row][col] == 'W':
        return 0

    visited.append(value)
    size = 1
    size+=explore(grid, row - 1, col, rows, cols, visited)
    size+=explore(grid, row, col - 1, rows, cols, visited)
    size+=explore(grid, row + 1, col, rows, cols, visited)
    size+=explore(grid, row, col + 1, rows, cols, visited)

    return size

          






grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

minimum_island(grid) # -> 4

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

minimum_island(grid) # -> 1

grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

minimum_island(grid) # -> 1