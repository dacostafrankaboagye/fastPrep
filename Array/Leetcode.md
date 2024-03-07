
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
    
  Explanation: 
  
    Mary is the tallest, followed by Emma and John.
  
  Example 2:
  
    Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
    Output: ["Bob","Alice","Bob"]
  
  Explanation: 
  
    The first Bob is the tallest, followed by Alice and the second Bob.
   
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
  
    - SparseVector(nums) Initializes the object with the vector nums
    - dotProduct(vec) Compute the dot product between the instance of SparseVectorand vec

  A sparse vector is a vector that has mostly zero values, you should store the sparse 
  vector efficiently and compute the dot product between two SparseVector.
  
  Follow up:
  
    What if only one of the vectors is sparse?
  
  Example 1:
    
    Input: 
      nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
    
    Output: 8
  
  Explanation: 
  
    v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
    
    v1.dotProduct(v2) = 1 * 0 + 0 * 3 + 0 * 0 + 2 * 4 + 3 * 0 = 8
  
  Example 2:
  
    Input: 
      nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
    
    Output: 0
  
  Explanation: 
  
    v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
    
    v1.dotProduct(v2) = 0 * 0 + 1 * 0 + 0 * 0 + 0 * 0 + 0 * 2 = 0
    
  Example 3:
  
    Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
    
    Output: 6
  
  Constraints:
    - n == nums1.length == nums2.length
    - 1 <= n <= 10^5
    - 0 <= nums1[i], nums2[i] <= 100

### solution - java
```java

/*
- create a hash map to hold {index:value} of non zero elements
- idea: multiplying by 0 -> result in 0 

e.g.           index   0 1 2 3 4 
        int[] nums1 = {1,0,0,2,3};
        int[] nums2 = {0,3,0,4,0};

        hashmap of nums1
        {   
            0 : 1,
            3 : 2,
            4 : 3
        }
        hashmap of nums2
        {
            1 : 3,
            3 : 4
        }

- now we have non zero element with index

- in the dotProduct method
    - after constructing the sparse vector, if any of the len of the sparsevec is 0; then return 0
    - loop through - say v1 : 
        if the key in v1 can also be found in v2 : then compute dot product and increment your result 
            - (what this means is that, the element in the v1 and v2 are not zero : that why their indexes appear in both v1 and v2)

*/

import java.util.HashMap;
import java.util.Map;


class SparseVector{

    HashMap<Integer, Integer> myHashMap;
    
    SparseVector(int[] nums){

        myHashMap = new HashMap<>();

        int i = 0;

        while(i < nums.length){
            if(nums[i] != 0){
                myHashMap.put(i, nums[i]);                
            }
            i++;
        }
    }

    // return the dot product of two sparse vector
    public int dotProduct(SparseVector vec){

        int result = 0;

        if(myHashMap.size() == 0 || vec.myHashMap.size() == 0){
            return 0;
        }

        for(int index : myHashMap.keySet()){
            if( vec.myHashMap.containsKey(index) ){
                result += myHashMap.get(index) * vec.myHashMap.get(index);
            }
        }
        return result;
    }

    // a method to print out the value 
    static void printSparseVector(SparseVector vec){
        for(Map.Entry<Integer,Integer> entry : vec.myHashMap.entrySet() ){
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println(key + " : " + value);
        }
        System.out.println("done");
    }
}


public class QnA{

    public static void main(String[] args) {

        /*
        // ans = 8
        int[] nums1 = {1,0,0,2,3};
        int[] nums2 = {0,3,0,4,0}; 
        */

        /*
        // ans = 0
        int[] nums1 = {0,1,0,0,0};
        int[] nums2 = {0,0,0,0,2};*/
        
        // ans = 6
        int[] nums1 = {0,1,0,0,2,0,0};
        int[] nums2 = {1,0,0,0,3,0,4};

        SparseVector v1 = new SparseVector(nums1);
        SparseVector v2 = new SparseVector(nums2);

        // SparseVector.printSparseVector(v1);
        // SparseVector.printSparseVector(v2);

        int ans = v1.dotProduct(v2);  
        System.out.println(ans);
    }
}

```

---


## 1502. Can Make Arithmetic Progression From Sequence - Easy

  A sequence of numbers is called an arithmetic progression if the difference between
  
  any two consecutive elements is the same.
  
  Given an array of numbers arr, return true if the array can be 
  
  rearranged to form an arithmetic progression. Otherwise, return false.
  
  Example 1:
  
    Input: arr = [3,5,1]
  
    Output: true
    
  Explanation: 
  
    We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

  
  Example 2:
  
    Input: arr = [1,2,4]
    Output: false
    
  Explanation: 
  
    There is no way to reorder the elements to obtain an arithmetic progression.

   
  Constraints:
  
    2 <= arr.length <= 1000
    
    -106 <= arr[i] <= 106

---
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
  ### solution - java
  ```java
  
  class Solution {
      public boolean canMakeArithmeticProgression(int[] arr) {
          Arrays.sort(arr);
          int fixedDiff = arr[1] - arr[0];
          for(int i=0; i<arr.length - 1; i++){
              if(arr[i+1] - arr[i] != fixedDiff){
                  return false;
              }
          }
          return true;
      }
  }
  ```
---

## 1874. Minimize Product Sum of Two Arrays - Medium

  The product sum of two equal-length arrays a and b 
  
  is equal to the sum of a[i] * b[i] 
  
  for all 0 <= i < a.length (0-indexed).
  
  For example, 
  
    if a = [1,2,3,4] and 
    b = [5,2,3,1], 
  
    the product sum would be 1*5 + 2*2 + 3*3 + 4*1 = 22.
  
  Given two arrays nums1 and nums2 of length n, 
  
  return the minimum product sum if you are allowed to rearrange the order of the elements in nums1.
  
  Example 1:
    
    Input: nums1 = [5,3,4,2], nums2 = [4,2,2,5]
    
    Output: 40
    
  Explanation: 
  
    We can rearrange nums1 to become [3,5,4,2]. 
    
    The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.

  Example 2:
  
    Input: nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]
    
    Output: 65
  
  Explanation: 
    We can rearrange nums1 to become [5,7,4,1,2].
    
    The product sum of [5,7,4,1,2] and [3,2,4,8,6] is 5*3 + 7*2 + 4*4 + 1*8 + 2*6 = 65.
  
  Constraints:
  
    n == nums1.length == nums2.length
    1 <= n <= 105
    1 <= nums1[i], nums2[i] <= 100

### solution - java

  ```java
  import java.util.Arrays;
  
  class Solution{
      public static int minProductSum(int[] nums1, int[] nums2) {
  
          int ans = 0;
  
          Arrays.sort(nums1);
          Arrays.sort(nums2);
  
          int i = 0;
          int j = nums2.length - 1;
  
          while(i < nums1.length && j >=0) {
              ans += + nums1[i] * nums2[j];
              i++;
              j--;
          }
  
          return ans;
      }
  }
  
  public class QnA{
  
      public static void main(String[] args) {
          // int[] nums1 = {5,3,4,2}, nums2 = {4,2,2,5};  // ans = 40
          int[] nums1 = {2,1,4,5,7}, nums2 = {3,2,4,8,6}; // ans = 65
  
          int result = Solution.minProductSum(nums1, nums2);
          System.out.println(result);    
      }
  }
  ```


---
## 53. Maximum Subarray - Medium

Given an integer array nums, find the 
subarray
with the largest sum, and return its sum.

 

Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6

    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

    Input: nums = [1]
    Output: 1

    Explanation: The subarray [1] has the largest sum 1.

Example 3:

    Input: nums = [5,4,-1,7,8]
    Output: 23

    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
 

Follow up:

    If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

### solution - python
```py

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            maxSum = max(currentSum, maxSum)
        return maxSum
```

### solution - java
```java

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
}

```

---


## 2455. Average Value of Even Numbers That Are Divisible by Three - Easy

Given an integer array nums of positive integers, 

return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n 

elements divided by n and rounded down to the nearest integer.

 

Example 1:

    Input: nums = [1,3,6,10,12,15]
    Output: 9
    Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.

Example 2:

    Input: nums = [1,2,4,7,10]
    Output: 0
    Explanation: There is no single number that satisfies the requirement, so return 0.
 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000

Hint

    What is the property of a number if it is divisible by both 2 and 3 at the same time?
    It is equivalent to finding all the numbers that are divisible by 6.

### solution - python
```py

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        the_sum = 0
        counter = 0
        for i in nums:
            if i % 6 == 0:
                the_sum += i
                counter += 1
        if counter == 0:
            return 0
        return the_sum // counter

```

---

## 2433. Find The Original Array of Prefix Xor - Medium

You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

    pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
    Note that ^ denotes the bitwise-xor operation.

    It can be proven that the answer is unique.

 

Example 1:

    Input: pref = [5,2,0,3,1]
    Output: [5,7,2,3,2]
    Explanation: From the array [5,7,2,3,2] we have the following:
    - pref[0] = 5.
    - pref[1] = 5 ^ 7 = 2.
    - pref[2] = 5 ^ 7 ^ 2 = 0.
    - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
    - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.


Example 2:


    Input: pref = [13]
    Output: [13]
    Explanation: We have pref[0] = arr[0] = 13.
 

Constraints:

    1 <= pref.length <= 105
    0 <= pref[i] <= 106

Hint 1

    Consider the following equation: x ^ a = b. How can you find x?

Hint 2

    Notice that arr[i] ^ pref[i-1] = pref[i]. This is the same as the previous equation.


### solution - python
```py

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) <= 1: 
            return pref
        ans = []
        ans.append(pref[0])
        for i in range(1, len(pref)):
            ans.append(pref[i] ^ pref[i-1])
        return ans


# Another solution
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        previousValue = pref[0]
        for i in range(1, len(pref)):
            pref[i] = pref[i] ^ previousValue # do the XOR opration
            previousValue = previousValue ^ pref[i] # get the value back [we are doing it in place]
        return pref
   

        

```

## 2114. Maximum Number of Words Found in Sentences - Easy

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

 

Example 1:

    Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

    Output: 6

Explanation: 

    - The first sentence, "alice and bob love leetcode", has 5 words in total.

    - The second sentence, "i think so too", has 4 words in total.

    - The third sentence, "this is great thanks very much", has 6 words in total.

    Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

Example 2:

    Input: sentences = ["please wait", "continue to fight", "continue to win"]

  Output: 3

Explanation: 

    It is possible that multiple sentences contain the same number of words. 

    In this example, the second and third sentences (underlined) have the same number of words.
  

Constraints:

    1 <= sentences.length <= 100

    1 <= sentences[i].length <= 100

    sentences[i] consists only of lowercase English letters and ' ' only.

    sentences[i] does not have leading or trailing spaces.

    All the words in sentences[i] are separated by a single space.

### solution - python
```py
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for sentence in sentences:
            the_len = len(sentence.split())
            maxWords = max(the_len, maxWords)
        return maxWords

'''
Hint 
  Process each sentence separately and
  count the number of words by looking for 
  the number of space characters in
  the sentence and adding it by 1.
'''

## Another solution
class Solution:
    def mostWordsFound(self, ss: List[str]) -> int:
        return max(s.count(" ") for s in ss) + 1
```

## 2114. 1929. Concatenation of Array - Easy

    Given an integer array nums of length n, you want to 
    create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

    Specifically, ans is the concatenation of two nums arrays.

    Return the array ans.

 

Example 1:

    Input: nums = [1,2,1]

    Output: [1,2,1,1,2,1]

    Explanation: The array ans is formed as follows:
    - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
    - ans = [1,2,1,1,2,1]

Example 2:

    Input: nums = [1,3,2,1]

    Output: [1,3,2,1,1,3,2,1]

    Explanation: The array ans is formed as follows:
    - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
    - ans = [1,3,2,1,1,3,2,1]
 

Constraints:

    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000

```java

```