import java.util.HashSet;
import java.util.Set;

class intersectionOfTwoArrays {
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
        Set<Integer> answerSet = new HashSet<>();
        for (Integer var : set1) {
            if (set2.contains(var)) {
                answerSet.add(var);
            }
        }
        int[] arr = new int[answerSet.size()];
        int j = 0;
        for (Integer val : answerSet) {
            arr[j] = val.intValue();
            j++;
        }
        return arr;
    }
}
