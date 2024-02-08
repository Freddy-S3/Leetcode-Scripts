package inPlaceArrayOperations;

public class greatestElementOnRight {
    public int[] replaceElements(int[] arr) {
        int big = -1;
        
        for(int i = arr.length - 1; i >= 0; i--){
            int temp = arr[i];
            arr[i] = big;
            if(temp > big){
                big = temp;
            }
                
        }
        
        return arr;
    }
}
