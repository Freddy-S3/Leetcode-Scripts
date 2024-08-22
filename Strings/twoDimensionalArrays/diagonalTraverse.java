package Strings.twoDimensionalArrays;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class diagonalTraverse {
        public int[] findDiagonalOrder(int[][] matrix) {
        if(matrix==null|| matrix.length==0) return new int[0];
        int N=matrix.length;
        int M=matrix[0].length;
        int[] res=new int[N*M];
        Map<Integer,List<Integer>>dict=new HashMap<>();
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                int sum=i+j;
                if(!dict.containsKey(sum))
                {
                    dict.put(sum, new ArrayList<>());
                }
                dict.get(sum).add(matrix[i][j]);
            }
        }
        int ctr=0;
        for(Map.Entry<Integer,List<Integer>> entry:dict.entrySet())
        {
            List<Integer> temp_list=new ArrayList<>();
            if(entry.getKey()%2==0)
            {
                temp_list=entry.getValue();
                Collections.reverse(temp_list);
            }
            else
            {
                 temp_list=entry.getValue(); 
            }
            for(int i=0;i<temp_list.size();i++)
            {
                res[ctr++]=temp_list.get(i);
            }
        }
        return res;
    }
}

/*
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
 */