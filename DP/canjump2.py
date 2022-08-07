import sys
class Solution(object):
    def jump(self, nums, flag):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = len(nums)
        if flag:
            return self.canJump_memo_shortest_dist(nums, 1, num)
        else:
            return self.canJump_memo_shortest_dist2(nums, 1, num)
        
    def canJump_memo_shortest_dist(self, values, pos, num, index_list = None, memo = None):
        if memo == None and index_list == None:
            index_list = []
            memo = {}
        
        if pos > num or (num == 1):
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

    def canJump_memo_shortest_dist2(self, values, pos, num, memo = None):
        if memo == None:
            memo = {}
        
        if pos > num or (num == 1):
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
            result = self.canJump_memo_shortest_dist2(values, position, num, memo)
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







import time
s = Solution()
nums = [2,3,1,1,4]
t1 = time.time()
print(s.jump(nums, 1))
print(time.time()-t1)

t1 = time.time()
print(s.jump(nums, 0))
print(time.time()-t1)
