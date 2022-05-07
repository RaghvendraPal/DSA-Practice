# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W


# def knapSack(W, wt, val, n):

# 	# Base Case
# 	if n == 0 or W == 0:
# 		return 0

# 	# If weight of the nth item is
# 	# more than Knapsack of capacity W,
# 	# then this item cannot be included
# 	# in the optimal solution
# 	if (wt[n-1] > W):
# 		return knapSack(W, wt, val, n-1)

# 	# return the maximum of two cases:
# 	# (1) nth item included
# 	# (2) not included
# 	else:
# 		return max(
# 			val[n-1] + knapSack(
# 				W-wt[n-1], wt, val, n-1),
# 			knapSack(W, wt, val, n-1))

# end of function knapSack



# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP

# driver code

# We initialize the matrix with -1 at first.
#Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

def knapsack(W, wt, val, n):

	# base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

	# choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                W-wt[n-1], wt, val, n-1),
            knapsack(W, wt, val, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(W, wt, val, n-1)
        return t[n][W]

# This code is contributed by Prosun Kumar Sarkar


# we can further improve the above Knapsack function's space
# complexity
def knapSack1(W, wt, val, n):

	K = [[0 for x in range(W+1)] for y in range(2)]
	
	# We know we are always using the the current row or
	# the previous row of the array/vector . Thereby we can
	# improve it further by using a 2D array but with only
	# 2 rows i%2 will be giving the index inside the bounds
	# of 2d array K
	for i in range(n + 1):
		for w in range(W + 1):
			if (i == 0 or w == 0):
				K[i % 2][w] = 0
			elif (wt[i - 1] <= w):
				K[i % 2][w] = max(
					val[i - 1]
					+ K[(i - 1) % 2][w - wt[i - 1]],
					K[(i - 1) % 2][w])

			else:
				K[i % 2][w] = K[(i - 1) % 2][w]

	return K[n % 2][W], K

# Driver Code



	# This code is contributed by ukasp.




print(knapsack(W, wt, val, n))
print("*"*100)
print(t)
print("*"*100)
P, K = knapSack1(W, wt, val, n)
print(P)
print("*"*100)
print(K)
print("*"*100)

# This code is contributed by Nikhil Kumar Singh
