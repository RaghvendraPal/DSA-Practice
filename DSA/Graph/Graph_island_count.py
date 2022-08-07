# island count
# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. 
# The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

def island_count(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = []
    count = 0
    # print("First Visit : ",visited)
    for row in range(rows):
        for col in range(cols):
            if explore(grid, row, col, rows, cols, visited):
                # print("Inside If")
                count += 1

    print("count : ", count)
    return count
            


def explore(grid, row, col, rows, cols, visited= None):
    value = str(row)+''+str(col)
    # print(visited)
    if visited is None:
        visited = []

    if row < 0 or col < 0 or row >= rows or col >= cols:
        return False

    if value in visited:
        return False

    if grid[row][col] == 'W':
        return False

    visited.append(value)

    explore(grid, row - 1, col, rows, cols, visited)
    explore(grid, row, col - 1, rows, cols, visited)
    explore(grid, row + 1, col, rows, cols, visited)
    explore(grid, row, col + 1, rows, cols, visited)

    return True

          






grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

island_count(grid) # -> 4

grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

island_count(grid) # -> 1

grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

island_count(grid) # -> 0