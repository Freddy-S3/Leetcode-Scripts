class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)

        if len(nums) < 3:
            return nums[length - 1]
        
        else:
            i = length - 1
            maxCounter = 1
            while i > 0 and maxCounter < 3:
                if nums[i-1] != nums[i]:
                    maxCounter +=1    
                i -= 1
            if maxCounter == 3:
                return nums[i]
            else:
                return nums[length - 1]


"""
Given an integer array nums, 
return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?
"""