class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums: 
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
        
        """
        length = len(nums)
        if length < 2:
            return length
        
        
        nums.sort()
        
        consecutive = 1
        counter = 1
        
        i = 0
        j = 1
        
        while j < length:
            print(nums[i], nums[j], counter)
            if nums[i] + 1 == nums[j]:
                counter += 1
                if counter > consecutive:
                    consecutive = counter
                
            elif nums[i] < nums[j]:
                counter = 1
            i += 1
            j += 1
        
        
        return consecutive
        """    
            
        


"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
1,762,536
Submissions
3,727,863
"""