package Strings.AdvancedStringsAndArrays;

import java.util.Arrays;
import java.util.List;

public class PascalsTriangle2 {
    public List<Integer> getRow(int rowIndex) {
      Integer[] result =  new Integer[rowIndex + 1];
      Arrays.fill(result, 0);
      result[0] = 1;
      for(int i = 1; i < rowIndex + 1; i++)
        for(int j = i; j >= 1; j--){
            result[j] += result[j - 1];
            System.out.println(Arrays.toString(result));        
        }
      return Arrays.asList(result);
    }
}

/*
 * Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
 */