

class Solution {
    public int maxSubArray(int[] nums) {
        int currentMax = nums[0];
        int maxSum = nums[0];
        for (int i=1;i<nums.length;i++){
            currentMax = Math.max(nums[i], nums[i]+currentMax);
            maxSum = Math.max(maxSum, currentMax);
        }
        return maxSum;
        
    
    }

    public int[] getConcatenation(int[] nums) {
        int nums_length = nums.length;
        int[] result = new int[nums_length*2];
        for(int i=0; i<nums_length; i++){
            result[i] = nums[i];
            result[nums_length+i] = nums[i];
        }
        return result;
        
    }
}

public class Test{

    public static void main(String[] args) {

        Solution s = new Solution();
        int[] test = {1,2,3};
        int[] ans = s.getConcatenation(test);
        for(int x : ans){
            System.out.println(x);
        }
        
        
    }
}