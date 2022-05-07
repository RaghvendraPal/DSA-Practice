def gridtraveller(m, n, memo: dict = {}):
    key = str(m) + "+" + str(n)
    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    
    memo[key] = gridtraveller(m-1, n, memo) + gridtraveller(m, n-1, memo)
    return memo[key]

print(gridtraveller(1, 1))
print(gridtraveller(2, 3))
print(gridtraveller(3, 2))
print(gridtraveller(3, 3))
print(gridtraveller(18, 18))




import numpy as np
def gridtraveller_table(m, n):

    table = [[ 0 for col in range(n+1)] for row in range(m+1)]
    table[1][1] = 1

    for row in range(m+1):
        for col in range(n+1):
            if col < n:
                table[row][col+1] += table[row][col]
            if row < m:
                table[row+1][col] += table[row][col]

    return table[m][n]

print("*"*100)
print(gridtraveller_table(1, 1))
print(gridtraveller_table(2, 3))
print(gridtraveller_table(3, 2))
print(gridtraveller_table(3, 3))
print(gridtraveller_table(18, 18))

