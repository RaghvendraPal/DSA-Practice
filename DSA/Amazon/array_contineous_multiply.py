# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, 
# and return the product. in O(N)  # Python3 program to find Maximum Product Subarray

# Returns the product
# of max product subarray.
def maxSubarrayProduct(arr, n):

	# max positive product
	# ending at the current position
	max_ending_here = arr[0]

	# min negative product ending
	# at the current position
	min_ending_here = arr[0]

	# Initialize overall max product
	max_so_far = arr[0]
	
	# /* Traverse through the array.
	# the maximum product subarray ending at an index
	# will be the maximum of the element itself,
	# the product of element and max product ending previously
	# and the min product ending previously. */
	for i in range(1, n):
		temp = max(max(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)
		min_ending_here = min(min(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)
		max_ending_here = temp
		max_so_far = max(max_so_far, max_ending_here)
	
	return max_so_far

# Driver code
arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print(f"Maximum Sub array product is {maxSubarrayProduct(arr, n)}")

# This code is contributed by shinjanpatra
