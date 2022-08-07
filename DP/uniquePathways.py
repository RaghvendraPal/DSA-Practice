# LeetCode
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28

class Solution(object):
    def uniquePaths(self, m, n, memo = {}):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        key = str(m)+" "+str(n)
        if key in memo:
            return memo[key]
        if m == 1 and n == 1:
            return 1
        elif n == 1 and m != 1:
            memo[key] = self.uniquePaths(m-1, n, memo)
            return memo[key]
        elif m == 1 and n != 1:
            memo[key] = self.uniquePaths(m, n-1, memo)
            return memo[key]
        
        memo[key] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)
        return memo[key]



# More Optimal

class Solution(object):
    def uniquePaths(self, m, n, memo = {}):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        key = str(m)+" "+str(n)
        if key in memo:
            return memo[key]
        if m == 1 and n == 1:
            memo[key] = 1
            return memo[key]
        if m == 0 or n == 0:
            memo[key] = 0
            return memo[key]
        
        memo[key] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)
        return memo[key]
        
        