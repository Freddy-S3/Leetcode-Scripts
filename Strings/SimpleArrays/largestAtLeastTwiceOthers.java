package Strings.SimpleArrays;

public class largestAtLeastTwiceOthers {
    public int dominantIndex(int[] nums) {
        int biggest = 0;
        int secondBig = 1;
        if (nums[biggest] < nums[secondBig]) {
            biggest = 1;
            secondBig = 0;
        }

        for (int index = 2; index < nums.length; index++){
            if (nums[index] > nums[biggest]){
                secondBig = biggest;
                biggest = index;
            }
            else if (nums[index] > nums[secondBig]) secondBig = index;
        }
        
        if (nums[secondBig] * 2 <= nums[biggest]) return biggest;
        else return -1;
    }
}

/*
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as 
much as every other number in the array. If it is, return the index of the largest element, 
or return -1 otherwise.

 

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
 

Constraints:

2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
 */