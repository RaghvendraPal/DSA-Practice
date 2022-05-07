# All number of solutions

all_solutions = []
def subset_sum(target, numbers, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        # print("sum(%s)=%s" % (partial, target))
        all_solutions.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers
        subset_sum(target,remaining , partial + [n]) 

# subset_sum(7, [2,4,3])
# print(all_solutions)
# print("*"*100)
# subset_sum(7, [5,3,4,7])
# print(all_solutions)
# print("*"*100)
# subset_sum(8, [2,3,5])
# print(all_solutions)
# print("*"*100)
# subset_sum(300, [7, 14])


# Unique Solutions
all_solutions = []
def subset_sum1(target, numbers, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print("sum(%s)=%s" % (partial, target))
        # all_solutions.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum1(target,remaining , partial + [n]) 

subset_sum1(7, [2,4,3])
# print(all_solutions)
# print("*"*100)
subset_sum1(7, [5,3,4,7])
# print(all_solutions)
# print("*"*100)
subset_sum1(8, [2,3,5])
# print(all_solutions)
print("*"*100)
# subset_sum(300, [7, 14])