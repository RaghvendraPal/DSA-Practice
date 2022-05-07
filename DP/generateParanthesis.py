value = []
def GenerateParanthesis(n, open, close, s = ""):
    if open == n and close == n:
        value.append(s)
        return

    if open < n:
        GenerateParanthesis(n, open+1, close, s+"(")
    
    if close < open:
        GenerateParanthesis(n, open, close+1, s+")")

n = 3
GenerateParanthesis(n, 0, 0)
for i in value:
    print(i)