# A = "AGGTAB"
# B = "GXTXAYB"
coins = [2, 3]
S = 8

memo = {}
# How many ways exist to generate the sum amount
def CoinChange(coins, S):
    if S < 0:
        return 0
    if S in memo:
        return memo[S]
    elif S == 0:
        return 1
    result = 0
    for coin in coins:
     
        result += CoinChange(coins, S-coin)
        memo[S] = result
    return memo[S]

print(CoinChange(coins, S))
print(memo)

# using memoization
memo = {}
def CoinChange1(coins, S):
    if S < 0:
        return 0
    elif S == 0:
        return 1
    if S in memo:
        return memo[S]
    result = 0
    for coin in coins:
        result += CoinChange1(coins, S-coin)
        memo[S] = result
    return memo[S]

print(CoinChange1(coins, S))
print(memo)


# Showing all the solution
def CoinChange_all_solution(coins, S, solution = []):
    if S < 0:
        return 0
    elif S == 0:
        print(solution)
        return 1
    result = 0
    for coin in coins:
        result += CoinChange_all_solution(coins, S-coin, solution + [coin])
    return result


print(CoinChange_all_solution(coins, S))



# Unique Solution:
n = len(coins)-1
def CoinChange_knapSack(coins, n, S):
    if S < 0 or n < 0:
        return 0
    if S == 0:
        return 1
    
    return CoinChange_knapSack(coins, n, S - coins[n]) + CoinChange_knapSack(coins, n-1, S)

print(CoinChange_knapSack(coins, n, S))

# Unique Solution:
memo = {}
n = len(coins)

def CoinChange_knapSack(coins, n, S, lookup = {}):
    key = str(n) + '+' +str(S)
    if S < 0 or n < 0:
        return 0
    if S == 0:
        return 1

    if key in lookup:
        return lookup[key]
    
    lookup[key] = CoinChange_knapSack(coins, n, S - coins[n]) + CoinChange_knapSack(coins, n-1, S)
    print(lookup)
    return lookup[key]

print(CoinChange_knapSack(coins, n-1, S))