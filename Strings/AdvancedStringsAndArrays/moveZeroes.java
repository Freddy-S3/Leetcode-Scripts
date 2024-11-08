package Strings.AdvancedStringsAndArrays;

public class moveZeroes {
    public void moveZero(int[] nums) {
        int lastNonZeroFoundAt = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                nums[lastNonZeroFoundAt++] = nums[i];                 
            }
        }
        for(; lastNonZeroFoundAt < nums.length; lastNonZeroFoundAt++){
            nums[lastNonZeroFoundAt] = 0;
        }
    }
}

/*
        int zeroCounter = 0;
        for(int i = 1; i < nums.length; i++){
            if(nums[i-1] == 0){
                zeroCounter++;
            }
            if(zeroCounter > 0){
                nums[i-zeroCounter] = nums[i];
            }
            
        }
        for(; zeroCounter > 0; zeroCounter--){
            nums[nums.length - zeroCounter] = 0;
        }
*/


/*
Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
 */
