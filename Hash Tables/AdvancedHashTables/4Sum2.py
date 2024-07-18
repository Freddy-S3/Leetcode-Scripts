import collections


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        AB = collections.Counter(a+b for a in nums1 for b in nums2)
        return sum(AB[-c-d] for c in nums3 for d in nums4)
        
        """
        def fourSumCount(self, A, B, C, D):
        count = 0
        num_dict = {}
        for i in C:
          for j in D:
            s = i + j
            if s in num_dict:
              num_dict[s] += 1
            else:
              num_dict[s] = 1

        for i in range(len(A)):
          for j in range(len(B)):
              target = 0 - (A[i]+B[j])
              if target in num_dict:
                count += num_dict[target]
        return count
        """


"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""