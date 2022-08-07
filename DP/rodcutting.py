from unittest import result

memo = {}
def rod_cutting(n, p):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0

    max_value = -1
    for val in range(1, n+1):
        # result = rod_cutting(n-val, p) + p[val]
        # if result > max_value:
        #     max_value = result
        max_value = max(max_value, rod_cutting(n-val, p)+p[val])

        # print("n : ", n, "val : ", val, "result : ", result, "max_value : ", max_value)

    memo[n] = max_value
    return max_value


def bestRodCutting(n, p: dict, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        if memo[n] is not None:
            return memo[n].copy()
        else:
            return None
    if n == 0: return 0, []
    if n < 0 : return 0, None

    max_value = -1
    Combination = None
    for val in range(1, n+1):
        remainder = n - val
        result, remainderCombination  =  bestRodCutting(remainder, p, memo)
        if remainderCombination is not None:
            remainderCombination.append(val)
            if (result > max_value):
                Combination = remainderCombination.copy()
                max_value = result
    # print(str(n) + "---------" + str(shortestCombination))
    if Combination:
        memo[n] = Combination.copy()
    else:
        memo[n] = None
    return max_value, Combination


profit = {
    1:1,
    2:5,
    3:8,
    4:9,
    5:10,
    6:17,
    7:17,
    8:20,
    9:24,
    10:30
}

print(rod_cutting(4, profit))
print(bestRodCutting(4, profit))
print(memo)