import java.util.HashSet;
import java.util.Set;

class intersectionOfTwoanswerays {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        for (int i : nums1) {
            set1.add(i);
        }
        Set<Integer> set2 = new HashSet<>();
        for (int i : nums2) {
            set2.add(i);
        }
        //Removed Duplicates using Hashset
        Set<Integer> duplicateSet = new HashSet<>();
        for (Integer var : set1) {
            if (set2.contains(var)) {
                duplicateSet.add(var);
            }
        }
        int[] answer = new int[duplicateSet.size()];
        int j = 0;
        for (Integer val : duplicateSet) {
            answer[j] = val.intValue();
            j++;
        }
        return answer;
    }
}

/*
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 */