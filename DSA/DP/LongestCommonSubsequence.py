# A = "AGGTAB"
# B = "GXTXAYB"
A = [1, 2, 3, 4, 1]
B = [3, 4, 1, 2, 1, 3]
n = len(A)
m =len(B)


t = [[-1 for i in range(m+1)] for j in range(n+1)]
def LCS(n, m, A, B):
    if n == 0 or m == 0:
        return 0
    if t[n][m] != -1:
        return t[n][m]
    elif A[n-1] == B[m-1]:
        t[n][m] = 1 + LCS(n-1, m-1, A, B)
        return t[n][m]
    t[n][m] = max(LCS(n-1, m, A, B), LCS(n, m-1, A, B))
    return t[n][m]

print(LCS(n, m, A, B))
print(t)

