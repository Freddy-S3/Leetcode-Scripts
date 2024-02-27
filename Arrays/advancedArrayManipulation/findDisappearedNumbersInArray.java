package advancedArrayManipulation;

import java.util.ArrayList;
import java.util.List;

public class findDisappearedNumbersInArray {
        public List<Integer> findDisappearedNumbers(int[] nums) {
        
        for(int number : nums){
            nums[Math.abs(number)-1] = -Math.abs(nums[Math.abs(number)-1]);
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < nums.length; i++){
            if (nums[i] > 0){
                result.add(i+1);
            }
        }
        return result;
    }
}

/*
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.
 */
