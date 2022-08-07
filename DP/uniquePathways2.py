class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        print(m, n)
        return self.uniquePaths(1, 1, m, n, obstacleGrid)
        
    def uniquePaths(self, start_row, start_col, m, n, obstacleGrid, memo = {}):
        key = str(start_row)+" "+str(start_col)
        if obstacleGrid[start_row-1][start_col-1]:
            memo[key] = 0
            return memo[key]
        if key in memo:
            return memo[key]
        if start_row == m and start_col == n:
            memo[key] = 1
            return memo[key]
        elif start_row != m and start_col == n:
            memo[key] = self.uniquePaths(start_row+1, start_col, m, n, obstacleGrid, memo)
            return memo[key]
        elif start_row == m and start_col != n:
            memo[key] = self.uniquePaths(start_row, start_col+1, m, n, obstacleGrid, memo)
            return memo[key]
        
        memo[key] = self.uniquePaths(start_row+1, start_col, m, n, obstacleGrid, memo) + self.uniquePaths(start_row, start_col+1, m, n, obstacleGrid, memo)
        print(memo)
        return memo[key]
        
s = Solution()
obstacleGrid = [[0,1],[0,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))