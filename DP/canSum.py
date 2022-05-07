def canSum(n, numbers: list, memo=None):
    if memo is None:
        memo = {}
    if n in memo: return memo[n]
    if n == 0: return True
    if n < 0 : return False

    for num in numbers:
        remainder = n - num
        if canSum(remainder, numbers, memo):
            memo[n] = True
            return True

    memo[n] = False
    return False

    

print(canSum(7, [2,4,3]))
print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7, 14]))