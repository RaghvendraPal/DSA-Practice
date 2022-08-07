# Given a string s, find the length of the longest substring without repeating characters.
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
                
        print(substr)
        return longest_string_l
        
# leetcode question : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.