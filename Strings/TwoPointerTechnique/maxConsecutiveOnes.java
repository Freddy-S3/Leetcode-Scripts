package Strings.TwoPointerTechnique;

public class maxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int sum = 0;
        for(int i = 0 ; i< nums.length; i ++){
            sum += nums[i];
            if(nums[i] == 0)    // reset sum to zero when encounters zeros
                sum = 0;
            else                // keep update max
                max = Math.max(max, sum);
        }
        return max;
    }
}

/*
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
 */