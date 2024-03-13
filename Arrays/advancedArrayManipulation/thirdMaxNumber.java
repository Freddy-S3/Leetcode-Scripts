package advancedArrayManipulation;

import java.util.Arrays;

public class thirdMaxNumber {
        public int thirdMax(int[] nums) {
        Arrays.sort(nums); 
        int Length = nums.length;
        if (Length < 3){
            return nums[Length - 1];
        }

        int maxCounter = 1;
        int i = Length - 1;
        
        while(i > 0 && maxCounter < 3){
            if (nums[i-1] != nums[i]){
                maxCounter++;
            }
            i--;
        }

        if (maxCounter ==3){
            return nums[i];
        }
        else{
            return nums[Length - 1];
        }
    }
}

/*
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
 */