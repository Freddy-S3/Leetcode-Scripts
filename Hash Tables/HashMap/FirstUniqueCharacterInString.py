class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #letter and occurences #can be done w/ count = collections.Counter(s)
        letterOccurence = {}
        
        for letter in s:
            if letter in letterOccurence:
                letterOccurence[letter] += 1
            else:
                letterOccurence[letter] = 1
        
        #run through first string
        for idx, character in enumerate(s):
            if letterOccurence[character] == 1:
                return idx
            else:
                continue
        
        return -1
        

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""