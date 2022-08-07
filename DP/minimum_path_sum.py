import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        time1 = time.time()
        print(self.minPath(1, 1, m, n, grid))
        print(time.time() - time1)
        time1 = time.time()
        print(self.minPathitr(m, n, grid))
        print(time.time() - time1)
    
    def minPath(self, start_row, start_col, m, n, grid, memo = {}):
        key = str(start_row)+" "+str(start_col)
        if key in memo:
            return memo[key]
        if start_row == m and start_col == n:
            memo[key] = grid[start_row-1][start_col-1]
            return memo[key]
        # elif start_row != m and start_col == n:
        #     # memo[key] = grid[start_row-1][start_col-1] + self.minPath(start_row+1, start_col, m, n, grid, memo)
        #     # return memo[key]
        # elif start_row == m and start_col != n:
        #     memo[key] = grid[start_row-1][start_col-1] + self.minPath(start_row, start_col+1, m, n, grid, memo)
        #     return memo[key]
        if start_row > m or start_col > n:
            memo[key] = sys.maxsize
            return memo[key]
        
        memo[key] = grid[start_row-1][start_col-1] + min(self.minPath(start_row+1, start_col, m, n, grid, memo),  self.minPath(start_row, start_col+1, m, n, grid, memo))
        # print(memo)
        return memo[key]

    def minPathitr(self, m , n, grid):
        if grid == None or len(grid) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])

        dp = [[-1 for i in range(n)] for j in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
    
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]


        for i in range(1, m):
            for j in range(1, n):
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                else:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
        # print(grid)
        # print(dp)
        return dp[-1][-1]


s = Solution()
import time

grid = [[1,2,3],[4,5,6]]
s.minPathSum(grid)
# print("*"*100)
# grid = [[1,3,1],[1,5,1],[4,2,1]]
# s.minPathSum(grid)
# print("*"*100)
# grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
# [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
# [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
# [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
# [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
# s.minPathSum(grid)
print("*"*100)

