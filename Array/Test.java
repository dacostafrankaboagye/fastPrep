import java.util.Arrays;

class Solution {

    public int[] buildArray(int[] nums) {

        int nums_length = nums.length;

        int[] result = new int[nums_length];

        for (int i = 0; i < nums_length; i++) {
            result[i] = nums[nums[i]];
        }

        return result;

    }
    public int[] buildArray_followUp(int[] nums) {

        // meta_data = a + bK 
        // storing
        // k = constant
        // a = nums[i]
        // b = nums[a] or nums[nums[i]]

        // recover
        // b = meta_data % K
        // a = meta_data / k

        int constant = 1001;

        for(int i=0; i<nums.length; i++){
            int a = nums[i];
            int b = nums[a];  // we need the original data, not the modified one = do a % constant to the the orignal
            int meta_data = (a) + (b % constant) * constant;
            nums[i] = meta_data;
        }
        for(int i=0; i<nums.length; i++){
            nums[i] = nums[i] / constant;
        }
        return nums;
        
    }
}

public class Test {

    public static void main(String[] args) {

        Solution s = new Solution();

        int[] test = {0,2,1,5,3,4};
        int[] ans = s.buildArray_followUp(test);
        System.out.println(Arrays.toString(ans));
        
    }
}