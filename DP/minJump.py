values = [2, 3, 1, 1, 4]
# values = [0]
values = [3,2,1]
def canJump_memo(values, pos, num):
    
    if pos > num or  not values[pos-1] or (num == 1):
        return None

    if pos == num:
        return []
    # key = str(pos) + '+' +str(num)
    # if key in memo:
    #     return memo[key]
    
    shortest_path = None
    for i in range(1, values[pos - 1]+1):
        position = pos+i
        result = canJump_memo(values, position, num)
        if result is not None:
            result.append(position)
            # print(result)
            if not shortest_path or len(shortest_path) > len(result):
            # memo[key] = True
                shortest_path = result.copy()
                # return shortest_path
    
    # memo[key] = False
    # print(memo)
    return shortest_path


def canJump_memo1(values, pos, num, index_list = [], memo = {}):
    
    if pos > num or  not values[pos-1] or (num == 1):
        return None

    if pos == num:
        return index_list

    key = str(pos) + '+' +str(num)
    if key in memo:
        return memo[key]
    
    shortest_path = None
    for i in range(1, values[pos - 1]+1):
        position = pos+i
        path_array = index_list + [position]
        result = canJump_memo1(values, position, num, path_array)
        if result is not None:
            # print(result)
            if not shortest_path or len(shortest_path) > len(result):
            # memo[key] = True
                shortest_path = result.copy()
                memo[key] = shortest_path.copy()
                # return shortest_path
    
    # memo[key] = False
    # print(memo)
    if shortest_path is not None:
        memo[key] = shortest_path.copy()
    else:
        memo[key] = None
    return memo[key]


import time

# t1 = time.time()
# num = len(values)
# print(canJump_memo1(values, 1, num))
# print(time.time()-t1)


def canJump_memo_shortest_dist(values, pos, num, index_list = [], memo = {}):
    if pos > num or not values[pos-1] or (num == 1):
        return 0

    if pos == num:
        return 1

    key = str(pos) + '+' +str(num)
    if key in memo:
        return memo[key]
    
    shortest_path = 0
    for i in range(1, values[pos - 1]+1):
        position = pos+i
        path_array = index_list + [position]
        result = canJump_memo_shortest_dist(values, position, num, path_array)
        if result:
            # print(result)
            if pos-1 != 0:
                result += 1 
            if not shortest_path or shortest_path > result:
            # memo[key] = True
                shortest_path = result
                memo[key] = shortest_path
                # return shortest_path
    
    # memo[key] = False
    # print(memo)
    if shortest_path is not None:
        memo[key] = shortest_path
    else:
        memo[key] = None

    print(memo)
    return memo[key]


import time

# t1 = time.time()
# num = len(values)
# # print(canJump_memo_shortest_dist(values, 1, num))
# print(time.time()-t1)



class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = len(nums)
        return self.canJump_memo_shortest_dist(nums, 1, num)
        
    def canJump_memo_shortest_dist(self, values, pos, num, index_list = [], memo = {}):
        if pos > num or  not values[pos-1] or (num == 1):
            return 0
        
        if pos == num:
            return 1
        # print(pos, num, values)

        key = str(pos) + '+' +str(num)
        if key in memo:
            return memo[key]

        shortest_path = 0
        for i in range(1, values[pos - 1]+1):
            position = pos+i
            path_array = index_list + [position]
            result = self.canJump_memo_shortest_dist(values, position, num, path_array, memo)
            if result:
                # print(result)
                if pos-1 != 0:
                    result += 1 
                if not shortest_path or shortest_path > result:
                # memo[key] = True
                    shortest_path = result
                    memo[key] = shortest_path
                    # return shortest_path

        # memo[key] = False
        # print(memo)
        if shortest_path is not None:
            memo[key] = shortest_path
        else:
            memo[key] = None

        # print(memo)
        return memo[key]

values = [3,2,1]
s = Solution()
print(s.jump(values))
