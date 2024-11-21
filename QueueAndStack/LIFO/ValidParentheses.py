class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #quick initial check
        if len(s)%2 != 0:
            return False
       
    
        dictionary = {"(":")", "{":"}", "[":"]"}
        
        queue = []
        for letter in s:
            if letter in "([{":
                queue.append(letter)
            elif letter in "]})":
                if queue == [] or dictionary[queue[-1]] != letter:
                    return False
                else:
                    queue.pop()
        
        return queue == []


"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""