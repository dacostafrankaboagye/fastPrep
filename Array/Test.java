import java.util.HashMap;
import java.util.Map;

class Solution {


    public int numIdenticalPairs(int[] nums) {
        int result = 0;
        int n = nums.length;
        HashMap<Integer, Integer> myHashMap = new HashMap<>();
        for(int i=0; i<n; i++){
            int temp =myHashMap.getOrDefault(nums[i], 0);
            result = result + temp;
            myHashMap.put(nums[i],  temp+1);
        }
        return result;

    }
}

public class Test {

    public static void main(String[] args) {

        Solution s = new Solution();

        int[] mytest = { 1, 2, 3, 1, 1, 3 };

        int result =  s.numIdenticalPairs(mytest);
        System.out.println("The number of identical pairs is " + result);


    }
}


/*

public class Test {

    public static void main(String[] args) {

        Solution s = new Solution();

        int[] mytest = { 1, 2, 3, 1, 1, 3 };

        HashMap<Integer, Integer> result = s.test(mytest);

        result.forEach((key, value)-> System.out.println(key + " : " + value));

    }
}
*/