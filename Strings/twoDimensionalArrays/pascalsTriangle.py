class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        answer = []
        
        for rows in range(numRows):
            builder = [1]
            
            for number in range(1, rows):
                builder.append(answer[rows-1][number-1] + answer[rows-1][number])
            
            if rows > 0:
                builder.append(1)
            
            answer.append(builder)
            
        return answer
                
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""