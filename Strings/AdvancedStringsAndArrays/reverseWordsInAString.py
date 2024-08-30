class Solution(object):
    def reverseWords(self, s):
        arr = list(s)
        self.reverse_string(arr, 0, len(arr)-1)
        self.reverse_word(arr)
        word = self.trim_sides(arr)
        res = self.trim_space(word)
        return ''.join(res)


    def reverse_string(self, arr, l, r):
        '''reverse a given string'''
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1 ; r -= 1
        return arr
    
    
    def reverse_word(self, arr):
        '''reverse every words in a string'''
        l, r = 0 , 0
        while r < len(arr):
            while r < len(arr) and not arr[r].isspace(): r += 1
            self.reverse_string(arr, l, r-1)
            r += 1; l = r
        return arr
    
    def trim_sides(self, arr):
        '''str.strip() basically'''
        if ''.join(arr).isspace(): return []
        l , r = 0, len(arr) - 1
        while l < r and arr[l].isspace(): l += 1
        while l < r and arr[r].isspace(): r -= 1
        return arr[l:r+1]
    
    def trim_space(self, word):
        '''remove duplicating space in a word'''
        if not word: return []
        res = [word[0]]            
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace(): continue
            res.append(word[i])
        return res

"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space 
in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it 
in-place with O(1) extra space?
"""