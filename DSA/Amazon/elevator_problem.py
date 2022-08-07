# Given an integer k and an array arr[] representing the destination floors for N people waiting currently at the ground floor 
# and k is the capacity of the elevator i.e. maximum number of people it can hold at the same time. It takes 1 unit time for the 
# elevator to reach any consecutive floor from the current floor. The task is to schedule the elevator in a way to minimize the 
# total time taken to get all the people to their destination floor and then return back to the ground floor.
# Examples: 
 

# Input: arr[] = {2, 3, 4}, k = 2 
# Output: 12 
# Second and the third persons (destination floors 3 and 4) shall go in the first turn taking 8 (4 + 4) unit time. 
# The only person left will take 2 unit time to get to the destination 
# And then the elevator will take another 2 unit time to get back to the ground floor. 
# Total time taken = 8 + 2 + 2 = 12
# Input: arr[] = {5, 5, 4}, k = 3 
# Output: 10 
# Every person can get on the elevator at the same time 
# Time required will be 10 (5 + 5). 
 


# Python3 implementation of the approach

# Function to return the minimum time taken
# by the elevator when operating optimally
def minTime(n, k, a) :
	
	# Sort in descending order
	a.sort(reverse = True);
	
	minTime = 0;

	# Iterate through the groups
	for i in range(0, n, k) :

		# Update the time taken for
		# each group
		minTime += (2 * a[i]);

	# Return the total time taken
	return minTime;

# Driver code
if __name__ == "__main__" :
	
	k = 2;
	arr = [ 2, 3, 4 ];
	n = len(arr) ;
	print(minTime(n, k, arr));
	
# This code is contributed by Ryuga
