class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_string_l = 0
        substr = ""
        length = 0
        for value in s:
            if value in substr:
                ind = substr.index(value)
                length = length - (ind)
                substr = substr[ind+1:]
                substr+=value
                # length = 1
            else:
                substr+=value
                length += 1
            if longest_string_l < length:
                longest_string_l = length
                
                
        return longest_string_l


s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))
        