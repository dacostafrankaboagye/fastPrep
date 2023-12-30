
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
---

## 2399. Check Distances Between Same Letters - Easy
  You are given a 0-indexed string s consisting of only lowercase English letters,
  where each letter in s appears exactly twice. 
  You are also given a 0-indexed integer array distance of length 26.
  Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
  In a well-spaced string, the number of letters between 
  the two occurrences of the ith letter is distance[i]. 
  If the ith letter does not appear in s, then distance[i] can be ignored.
  
  Return true if s is a well-spaced string, otherwise return false.
  
  Example 1:
  
  Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  Output: true
  Explanation:
  - 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
  - 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
  - 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
  Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
  Return true because s is a well-spaced string.
  
  Example 2:
  
  Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  Output: false
  Explanation:
  - 'a' appears at indices 0 and 1 so there are zero letters between them.
  Because distance[0] = 1, s is not a well-spaced string.
   
  Constraints:
  
  2 <= s.length <= 52
  s consists only of lowercase English letters.
  Each letter appears in s exactly twice.
  distance.length == 26
  0 <= distance[i] <= 50
  
  ### Solution - python
  ```py
  class Solution:
      def checkDistances(self, s: str, distance: List[int]) -> bool:
          my_dict = {}
          for i in range(len(s)):
              letter = s[i]
              if letter in my_dict:
                  calculated_distance = i - my_dict[letter] - 1
                  distance_in_list = distance[ord(letter) - 97]
                  if calculated_distance == distance_in_list:
                      my_dict.pop(letter)
                  else:
                      return False
              else:
                  my_dict[letter] = i
          if my_dict: return False
          else: return True
  ```
  ### Solution - java [converting the python code]
  ```java
  class Solution {
      public boolean checkDistances(String s, int[] distance) {
          HashMap<Character, Integer> my_dict = new HashMap<>();
          for(int i=0; i<s.length(); i++){
              char letter = s.charAt(i);
              if(my_dict.containsKey(letter)){
                  int calculated_distance = i - my_dict.get(letter) - 1;
                  int distance_in_list = distance[(int)letter - 97]; // you can do letter - 'a'
                  if(calculated_distance == distance_in_list){
                      my_dict.remove(letter);
                  }else{
                      return false;
                  }
  
              }else{
                  my_dict.put(letter, i);
              }
          }
          if(my_dict.isEmpty()){
              return true;
          }else{
              return false;
          }
          // can be replaced with >> return my_dict.isEmpty()
      }
  }
  ```

---

## LeetCode 1570. Dot Product of Two Sparse Vectors - medium
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums

dotProduct(vec) Compute the dot product between the instance of SparseVectorand vec

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
Follow up: What if only one of the vectors is sparse?

Example 1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]

Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example 2:
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example 3:
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100

- Your SparseVector object will be instantiated and called as such:
- SparseVector v1(nums1);
- SparseVector v2(nums2);
- int ans = v1.dotProduct(v2);


---


## 1502. Can Make Arithmetic Progression From Sequence - Easy
  A sequence of numbers is called an arithmetic progression if the difference between
  any two consecutive elements is the same.
  Given an array of numbers arr, return true if the array can be 
  rearranged to form an arithmetic progression. Otherwise, return false.
  
  Example 1:
  
  Input: arr = [3,5,1]
  
  Output: true
  
  Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

  
  Example 2:
  
  Input: arr = [1,2,4]
  Output: false
  Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

   
  Constraints:
  
  2 <= arr.length <= 1000
  
  -106 <= arr[i] <= 106
  
  ### solution - python
  ```py
  
  class Solution:
      def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
          arr.sort()
          fixed_diff = arr[1] - arr[0]
          for i in range(0, len(arr)-1):
              if arr[i+1] - arr[i] != fixed_diff:
                  return False
          return True
      
  ```
