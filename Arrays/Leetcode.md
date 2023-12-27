
## 1480. Running Sum of 1d Array - Easy

  Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
  
  Return the running sum of nums. 
  
  Example 1:
  
  Input: nums = [1,2,3,4]
  Output: [1,3,6,10]
  Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
  Example 2:
  
  Input: nums = [1,1,1,1,1]
  Output: [1,2,3,4,5]
  Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
  Example 3:
  
  Input: nums = [3,1,2,10,1]
  Output: [3,4,6,16,17]
  
  Constraints:
  
  1 <= nums.length <= 1000
  -10^6 <= nums[i] <= 10^6

  ### Solution - java
  ```java

  /*
  decalre a variable - sum and int[] result
  loop through and add each nums[i] to sum -> then add it to result[]
  */
  
  class Solution {
  
      public int[] runningSum(int[] nums) {
          int[] result = new int[nums.length];
          int theSum = 0;
          for(int i=0; i<nums.length; i++){
              theSum += nums[i];
              result[i] = theSum;
          }
          return result;
      }
  }
  
  
  /*
  in place
  */
  class Solution {
  
      public int[] runningSum(int[] nums) {
          for(int i=1; i<nums.length; i++){
              nums[i] = nums[i-1] + nums[i];
          }
          return nums;
      }
  
  }
 ```
### Solution - python
  ```py
  
  class Solution:
      def runningSum(self, nums: List[int]) -> List[int]:
          for i in range(1, len(nums)):
              nums[i] = nums[i-1] + nums[i]
          return nums
  
  ```

---

## 2418. Sort the People - Easy

  You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
  
  For each index i, names[i] and heights[i] denote the name and height of the ith person.
  
  Return names sorted in descending order by the people's heights.
  
  Example 1:
  
  Input: names = ["Mary","John","Emma"], heights = [180,165,170]
  Output: ["Mary","Emma","John"]
  Explanation: Mary is the tallest, followed by Emma and John.
  Example 2:
  
  Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
  Output: ["Bob","Alice","Bob"]
  Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
   
  Constraints:
  
  n == names.length == heights.length
  1 <= n <= 103
  1 <= names[i].length <= 20
  1 <= heights[i] <= 105
  names[i] consists of lower and upper case English letters.
  All the values of heights are distinct.
  
  ### solution -python
  ```py
  
  class Solution:
      def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
          my_dict = { heights[i]:names[i]  for i in range(len(heights))}
          my_dict = dict(sorted(my_dict.items(), reverse=True))
          return my_dict.values()
          
        
  ```
