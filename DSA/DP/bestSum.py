# 1 method
# def howSum(n, numbers: list, memo:dict = {}, val:list = []):
#     # print(n, memo)
#     if n in memo: return memo[n]
#     if n == 0: return True
#     if n < 0 : return False

#     for num in numbers:
#         remainder = n - num
#         if howSum(remainder, numbers, memo):
#             memo[n] = True
#             val.append(num)
#             return True, val

#     memo[n] = False
#     return False

# 2 method

def bestSum(n, numbers: list, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        if memo[n] is not None:
            return memo[n].copy()
        else:
            return None
    if n == 0: return []
    if n < 0 : return None

    shortestCombination = None
    for num in numbers:
        remainder = n - num
        remainderCombination  =  bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            remainderCombination.append(num)
            if (not shortestCombination) or (len(remainderCombination ) <= len(shortestCombination)):
                shortestCombination = remainderCombination.copy()
    # print(str(n) + "---------" + str(shortestCombination))
    if shortestCombination:
        memo[n] = shortestCombination.copy()
    else:
        memo[n] = None
    return shortestCombination

# def bestSum(targetSum, numbers, memo={}):
#     if targetSum in memo:
#         return memo[targetSum]
#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return None

#     shortestCombination = None
#     for num in numbers:
#         remainder = targetSum - num
#         remainderCombination = bestSum(remainder, numbers, memo)

#         if remainderCombination is not None:
#             combination = remainderCombination + [num]
#             if shortestCombination is None or len(combination) < len(shortestCombination):
#                 shortestCombination = combination.copy()

#     print(str(targetSum) + "---------" + str(shortestCombination))
#     if shortestCombination:
#         memo[targetSum] = shortestCombination.copy()
#     else:
#         memo[targetSum] = None
#     return shortestCombination

    
print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))

# print([]!= None)
print(bestSum(100, [1,2,5,25]))

# Time Complexity O(n*m*m) here second m is the result size
# Space Complexity O(m*m)
# because memo will also have arrays value

# brute force
# time complexity O(n^m * m)
# Space O(m*m)