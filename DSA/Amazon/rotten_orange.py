# Python3 program to rot all
# oranges when u can move
# in all the four direction
# from a rotten orange
R = 3
C = 5

# Check if i, j is under the
# array limits of row and
# column
def issafe(i, j):

	if (i >= 0 and i < R and
		j >= 0 and j < C):
		return True
	return False

def rotOranges(v):

    changed = False
    no = 2
    t = 0
    while (True):
        for i in range(R):
            for j in range(C):

				# Rot all other oranges
				# present at (i+1, j),
				# (i, j-1), (i, j+1),
				# (i-1, j)
                if (v[i][j] == no):
                    if (issafe(i + 1, j) and
                        v[i + 1][j] == 1) and v[i + 1][j] != 2:
                        v[i + 1][j] += 1
                        changed = True

                    if (issafe(i, j + 1) and
                        v[i][j + 1] == 1) and v[i][j + 1] != 2:
                        v[i][j + 1] += 1
                        changed = True

                    if (issafe(i - 1, j) and
                        v[i - 1][j] == 1) and v[i - 1][j] != 2:
                        v[i - 1][j] += 1
                        changed = True

                    if (issafe(i, j - 1) and
                        v[i][j - 1] == 1) and v[i][j - 1] != 2:
                        v[i][j - 1] += 1
                        changed = True

		# if no rotten orange found
		# it means all oranges rottened
		# now
        t += 1
        if (not changed):
            break
        changed = False

    for i in range(R):
        for j in range(C):

            # if any orange is found
            # to be not rotten then
            # ans is not possible
            if (v[i][j] == 1):
                return -1

	# Because initial value
	# for a rotten orange was 2
    return t

# Driver function
if __name__ == "__main__":

	v = [[2, 1, 0, 2, 1],
		[0, 0, 1, 2, 1],
		[1, 0, 0, 2, 1]]

	print("Max time incurred: ",
		rotOranges(v))

# This code is contributed by Chitranayal
