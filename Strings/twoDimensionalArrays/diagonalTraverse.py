class Solution:
    def findDiagonalOrder(self, matrix):

        if not matrix or not matrix[0]:
            return []

        N, M = len(matrix), len(matrix[0])

        row, column = 0, 0
        
        direction = 1
        
        result = []
        
        while row < N and column < M:
            
            result.append(matrix[row][column])

            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)
            
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
                
                if direction:
                    
                    row += (column == M - 1)
                    print(row)
                    column += (column < M - 1)
                else:
                    
                    column += (row == N - 1)
                    row += (row < N - 1)
                    print(row)
                    
                direction = 1 - direction        
            else:
                row = new_row
                column = new_column
                        
        return result 
    
"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""