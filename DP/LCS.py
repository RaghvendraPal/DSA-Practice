def LCS(X, Y, m, n, dp, s = ""):
    if dp[m][n] != -1:
        return dp[m][n]
        
    if m == 0 or n == 0:
        return 0
    
    elif X[m-1] == Y[n-1]:
        # s+=X[m-1]
        dp[m][n] = 1 + LCS(X, Y, m-1, n-1, dp, s)
        return dp[m][n]

    else:
        dp[m][n] = max(LCS(X, Y, m-1, n, dp, s), LCS(X, Y, m, n-1, dp, s))
        return dp[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
dp = [[-1 for i in range(n+1)] for i in range(m+1)]
print(LCS(X, Y, m, n, dp)) 
print(dp)