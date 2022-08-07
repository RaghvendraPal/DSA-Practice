class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

# Max Level sum
def maxlevelSum(tree, level = 0, max_sum_value = 0, max_sum_level = 0):
    if not tree:
        return  max_sum_level
    sum = 0
    try:
        sum = levels[level]
    except:
        levels.append(0)
        sum = levels[level]

    sum += tree.data
    # print("Level : ", level, "Value : ", sum)
    levels[level] = sum

    # print(max_sum_value, sum)
    if sum > max_sum_value:
        max_sum_value = sum
        max_sum_level = level

    max_sum_level = maxlevelSum(tree.left, level+1, max_sum_value, max_sum_level)
    max_sum_level = maxlevelSum(tree.right, level+1, max_sum_value, max_sum_level)

    return max_sum_level


def levelSum(tree, level = 0, levels = None):
    if levels == None:
        levels = []
    if not tree:
        return
    sum = 0
    try:
        # print(level, levels)
        sum = levels[level]
    except:

        levels.append(0)
        # print(level, levels)
        sum = levels[level]

    sum += tree.data
    # print("Level : ", level, "Value : ", sum)
    levels[level] = sum

    # print(max_sum_value, sum)

    levelSum(tree.left, level+1, levels)
    levelSum(tree.right, level+1, levels)

    return levels


def vertical_sum(tree, hl, memo = None):
    if not memo:
        memo = {}

    if not tree:
        return memo
    memo = vertical_sum(tree.left, hl-1, memo)

    if hl in memo:
        memo[hl]+= tree.data
    else:
        memo[hl] = tree.data
    # print("hl : ", hl, memo)
    memo = vertical_sum(tree.right, hl+1, memo)

    return memo

    


tree = Node(2)
tree.left = Node(3)
tree.right = Node(1)
tree.left.left = Node(-1)
tree.left.right = Node(4)
tree.right.left = Node(-2)
tree.right.right = Node(7)
levels = []
print(maxlevelSum(tree))
print(levelSum(tree))
print(levels)
memo = vertical_sum(tree, 0)
# print(memo)
for val in memo.values():
    print(val, end = " ")

print("\n")
levels = []
# print(leaf_sum(tree))

#             2
    
#     3               1

# -1      4       -2      7

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
print(maxlevelSum(tree))
print(levelSum(tree))
print(levels)
memo = vertical_sum(tree, 0)
# print(memo)
for val in memo.values():
    print(val, end = " ")

#             1
    
#     2               3

# 4      5       6       7
