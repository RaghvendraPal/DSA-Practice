# Python3 program to implement traveling salesman
# problem using naive approach.
# Python3 implementation of the approach
V = 4
answer = []

# Function to find the minimum weight
# Hamiltonian Cycle
def tsp(graph, v, currPos, n, count, cost):

	# If last node is reached and it has
	# a link to the starting node i.e
	# the source then keep the minimum
	# value out of the total cost of
	# traversal and "ans"
	# Finally return to check for
	# more possible values
	if (count == n and graph[currPos][0]):
		answer.append(cost + graph[currPos][0])
		return

	# BACKTRACKING STEP
	# Loop to traverse the adjacency list
	# of currPos node and increasing the count
	# by 1 and cost by graph[currPos][i] value
	for i in range(n):
		if (v[i] == False and graph[currPos][i]):
			
			# Mark as visited
			v[i] = True
			tsp(graph, v, i, n, count + 1,
				cost + graph[currPos][i])
			
			# Mark ith node as unvisited
			v[i] = False

# Driver code


# This code is contributed by mohit kumar


V = 4
def TSP(current, start, nodes, graph, n):
    # nodes = nodes.copy()
    # print("Before 1",nodes)
    nodes[current] = False
    print("Before 2 ",nodes, "(",current, ",", n, ")")
    if not n-1:
        nodes[current] = True
        return graph[current][start]

    min_cost = None
    # print(nodes)
    for val in range(V):
        if nodes[val]:
            print(val)
            result = graph[current][val] + TSP(val, start, nodes, graph, n-1)
            print(result, min_cost)
            nodes[val] = True
            print("back : ",nodes)
            if not min_cost or result < min_cost:
                min_cost = result

    return min_cost

# n is the number of nodes i.e. V
if __name__ == '__main__':
    n = 4
    graph= [[ 0, 10, 15, 20 ],
            [ 10, 0, 35, 25 ],
            [ 15, 35, 0, 30 ],
            [ 20, 25, 30, 0 ]]

    # Boolean array to check if a node
    # has been visited or not
    v = [False for i in range(n)]

    # Mark 0th node as visited
    v[0] = True

    # Find the minimum weight Hamiltonian Cycle
    tsp(graph, v, 0, n, 1, 0)

    # ans is the minimum weight Hamiltonian Cycle
    print(min(answer))

    s = 0
    nodes = [True for i in range(n)]
    current = 0

    print(TSP(current, current, nodes, graph, n))
