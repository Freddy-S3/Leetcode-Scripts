package Strings.SimpleStrings;

public class implementStr {
    public int strStr(String haystack, String needle){
        if (haystack == null || needle == null ||haystack.length() < needle.length())
            return -1;
        //generate next array, need O(n) time
        int i = -1, j = 0, m = haystack.length(), n = needle.length();
        int[] next = new int[n];
        if (next.length > 0) 
            next[0] = -1;
        while (j < n - 1) {
            if (i == -1 || needle.charAt(i) == needle.charAt(j))
                next[++j] = ++i;
            else 
                i = next[i];
        }
        //check through the haystack using next, need O(m) time
        i = 0; j = 0;
        while (i < m && j < n) {
            if (j == -1 || haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
            }
            else 
                j = next[j];
        }
        if (j == n)
            return i - j;
        return -1;
    }
}
/*
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
 */