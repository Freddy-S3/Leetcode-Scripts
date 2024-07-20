class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        leftPointer = 0
        maxSize = 0
        alphadict = {}
        
        for index, letter in enumerate(s):
            if letter in alphadict:
                leftPointer = max(leftPointer, alphadict[letter] + 1)
            
            alphadict[letter] = index

            currentSize = index - leftPointer + 1
            if currentSize > maxSize:
                maxSize = currentSize

        return maxSize
                


"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
   Hide Hint #1  
Generate all possible substrings & check for each substring if it's valid and keep updating maxLen accordingly.
"""