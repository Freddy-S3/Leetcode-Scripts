import java.util.HashSet;
import java.util.Set;



public class HappyNumber {
    public boolean isHappy(int n) {
        Set<Integer> inLoop = new HashSet<Integer>();
        int total,remain;
        while (inLoop.add(n)) {
            total = 0;
            while (n > 0) {
                remain = n%10;
                total += remain*remain;
                n /= 10;
            }
            if (total == 1)
                return true;
            else
                n = total;
    
        }
        return false;
    
    }
}
