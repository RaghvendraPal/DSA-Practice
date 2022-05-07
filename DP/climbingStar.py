



def climb(n, lookup = {}):
    if n == 0:
        return True
    
    if n < 0:
        return False

    if n in lookup:
        return lookup[n]

    lookup[n] = climb(n-1) or climb(n-2)
    print(lookup)
    return lookup[n]


# n = 2
# print(climb(n))

solutions = []
def climb_distinct(S, target, lookup = {}, path = []):
    if S == target:
        solutions.append(path)
    
    if S > target:
        return

    # if n in lookup:
    #     return lookup[n]
    for i in range(1, 3):
        result = climb_distinct(S+i, target, lookup, path + [i])

    return

n = 4
climb_distinct(0, n)
print(solutions)

def climb_ways(target, memo = {}):
    if target == 0:
        return 1

    if target < 0:
        return False 

    if target in memo: return memo[target]
    ways = 0
    for i in range(1, 3):
        result = climb_ways(target-i)
        if result:
            ways += result

    memo[target] = ways
    print(memo)
    return ways

n = 4
print(climb_ways(n))
# print(solutions)
