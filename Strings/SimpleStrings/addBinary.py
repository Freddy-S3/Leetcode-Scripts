class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        sum= ""
        aIndex = len(a)-1
        bIndex = len(b)-1
        
        while aIndex >= 0 or bIndex >= 0 or carry:
            if aIndex >= 0:
                carry += int(a[aIndex])
                
            if bIndex >= 0:
                carry += int(b[bIndex])
                
            sum = str(carry%2) + sum
            carry //= 2
            
            aIndex -= 1
            bIndex -= 1
            
        return sum

"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""