class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        length = len(arr)
        
        
        if length < 2 or arr == None:
            return False
        
        for i in range(length - 1):
            for j in range(i+1,length):
                
                if arr[i] < 0 and arr[j] < 0:
                    if arr[i] < arr[j]:
                        if arr[j] * 2 == arr[i]:
                            return True
                        else:
                            continue
                    elif arr[i] > arr[j]:
                        if arr[i] * 2 == arr[j]:
                            return True
                        else:
                            continue
                
                elif arr[i] > 0 and arr[j] > 0:
                    if arr[i] < arr[j]:
                        if arr[i] * 2 == arr[j]:
                            return True
                        else:
                            continue
                    if arr[i] > arr[j]:
                        if arr[j] * 2 == arr[i]:
                            return True
                        else:
                            continue
                
                elif arr[i] == arr[j]:
                    if arr[i] == 0:
                        return True
                    else:
                        continue
                else:
                    continue
            #return False
        return False


"""
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
"""