# 1 method
def howSum(n, numbers: list, memo=None, val:list = []):
    # print(n, memo)
    if memo is None:
        memo = {}
    if n in memo: return memo[n]
    if n == 0: return True
    if n < 0 : return False

    for num in numbers:
        remainder = n - num
        if howSum(remainder, numbers, memo):
            memo[n] = True
            val.append(num)
            return True, val

    memo[n] = False
    return False

# 2 method

def howSum(n, numbers: list, memo:dict = {}):
    # print(n, memo)
    if n in memo: return memo[n]
    if n == 0: return []
    if n < 0 : return None

    for num in numbers:
        remainder = n - num
        result =  howSum(remainder, numbers, memo)
        if result != None:
            result.append(num)
            memo[n] = result
            return memo[n]

    memo[n] = None
    return None

    
print(howSum(7, [2,4,3]))
# print(howSum(7, [5,3,4,7]))
# print(howSum(7, [2,4]))
# print(howSum(8, [2,3,5]))
# print(howSum(8, [3,5,2]))
# print(howSum(300, [7, 14]))

# Time Complexity O(n*m*m) here second m is the result size
# Space Complexity O(m*m)
# because memo will also have arrays value

# brute force
# time complexity O(n^m * m)
# Space O(m)