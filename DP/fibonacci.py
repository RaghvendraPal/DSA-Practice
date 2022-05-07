
# memoization
def fibonacci(n, memo: dict = {}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1

    if n == 0:
        return 0
    
    memo[n] = fibonacci(n-1)+fibonacci(n-2)
    return memo[n]

# Tabularization

def fibonacci_table(n, table=None):
    if table is None:
        table = [0]*(n+1)
        table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i-1]+table[i-2]
    return table[-1]


    


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(20))
print(fibonacci(50))

print(fibonacci_table(5))
print(fibonacci_table(10))
print(fibonacci_table(20))
print(fibonacci_table(50))