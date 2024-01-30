class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index1 = m-1
        index2 = n-1
        j = m + n -1
        
        while j >=0:
            
            # when nums1 is not there, then we need the below condition.
            # edge case nums1 =[0,0,0,0,0], m=0, nums2=[1,2,3,4,5], n=5
            if index2>=0 and (m==0 or nums2[index2] >= nums1[index1]):
                nums1[j] = nums2[index2]
                index2 -=1
                print("index2:", index2)
                print("first:", nums1)
                
            # for the condition when there is no element in array 2, 
            # then the value os index2 is 0, so we need a conditon index2> -1 
            # to carry out the implementation without occuring to index out of range error.
            # edge case nums1= [1], m=1, nums2= [], n=0
            elif index2 > -1 and nums1[index1] > nums2[index2]:
                nums1[j], nums1[index1] = nums1[index1], nums1[j]
                
                # if there are any more indices left to traverse, then decrement 
                # the index or else keep the index same.
                # Edge case: nums1 =[2,0], m=1, nums2=[1], n =1
                if index1:
                    index1 -=1
                print("index1:", index1)
                print("second:", nums1)
            j -=1
            
        # at the end if there is a negative value and still there are elements 
        # in nums2 then add those to nums1
        # Edge case:
        # nums1 =[0,0,3,0,0,0,0,0,0], m =3
        # nums2 = [-1,1,1,1,2,3], n =6
        if index2 >-1:
            for i in range(index2 +1):
                nums1[i] = nums2[i]

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""