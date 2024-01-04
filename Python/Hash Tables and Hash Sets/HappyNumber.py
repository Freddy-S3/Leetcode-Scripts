class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        answerHash = set()
        answerHash.add(n)
        
        numberList = [int(i) for i in str(n)]
        
        while numberList != [1]:
            total = 0
            for number in numberList:
                total += number*number
            
            #check if answer appeared previously
            if total in answerHash:
                return False
            else:
                answerHash.add(total)
            
            numberList = [int(i) for i in str(total)]
            
        return True
    
"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""