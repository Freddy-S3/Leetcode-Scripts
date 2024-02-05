public class validMountainArray {
    public boolean mountainArrayCheck(int[] arr) {
        int i = 0;
        boolean second = false;
        int size = arr.length - 1;
        
        if(arr.length < 3){
            return false;
        }
        
        if(arr[i] < arr[i+1]){
            while(i < size && arr[i] < arr[i+1]){
                i++;
            }
            while(i < size && arr[i] > arr[i+1]){
                i++;
                second = true;
            }
            if(i == size  && second == true){
                return true;
            }
        } 
        return false;
    }
}

/*
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
 */
