public class elementAndDoubleExist {
    public boolean checkIfExist(int[] arr) {
        int iVar = 0;
        int jVar = 0;
        
        for(int i=0; i < arr.length - 1; i++){
            for(int j = i+1; j < arr.length; j++){
                iVar = arr[i];
                jVar = arr[j];
                if(iVar < 0 && jVar < 0){
                    iVar = Math.abs(iVar);
                    jVar = Math.abs(jVar);
                }
                
                if(iVar >= 0 && jVar >= 0){
                    if(iVar > jVar){
                        int temp = iVar;
                        iVar = jVar;
                        jVar = temp;
                    }
                    
                    if(iVar * 2 == jVar){
                        return true;
                    }
                }

                    
             
            }
        }
        
        
        
        return false;
    }
}

/*
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
 */