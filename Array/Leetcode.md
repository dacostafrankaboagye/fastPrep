# General   

    Sum of the First n Natural Numbers.
    
    1+ 2+ ... + n 
    
    = n(n+1) / 2, for n a natural number
---

    If a number appears n times, then 
    
    n * (n – 1) // 2 good pairs can be made with this number


---

## 1470. Shuffle the Array Easy

	Given the array nums consisting of 2n elements in the 
 	form [x1,x2,...,xn,y1,y2,...,yn].

	Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 

Example 1:

	Input: nums = [2,5,1,3,4,7], n = 3
	Output: [2,3,5,4,1,7] 
	
 	Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 
  	then the answer is [2,3,5,4,1,7].
 
Example 2:

	Input: nums = [1,2,3,4,4,3,2,1], n = 4
	Output: [1,4,2,3,3,2,4,1]

Example 3:

	Input: nums = [1,1,2,2], n = 2
	Output: [1,2,1,2]
 

Constraints:

	1 <= n <= 500
	nums.length == 2n
	1 <= nums[i] <= 10^3
 
```java

class Solution {
    public int[] shuffle(int[] nums, int n) {
        int left = 0;
        int right = n;
        int[] numsCopy = Arrays.copyOf(nums, nums.length);
        for(int i=0; i<nums.length; i++){
           if(i % 2 == 0){
            // odd -> pick from the 0..n
            numsCopy[i] = nums[left];
            left++;
           }else{
            // even -> pick from 
            numsCopy[i] = nums[right];
            right++;
           }
        }

        return numsCopy;
        
    }
}


class Solution {

    public int[] shuffle(int[] nums, int n) {
        int[] result = new int[n*2];
        for(int i=0; i<n; i++){
            result[2*i] = nums[i];
            result[(2*i) + 1] = nums[i+n];
        }
        return result;

    }
}


```


---

## 3190. Find Minimum Operations to Make All Elements Divisible by Three - Easy

	You are given an integer array nums. In one operation, you can 
 	add or subtract 1 from any element of nums.
	
	Return the minimum number of operations to make all elements of 
 	nums divisible by 3.
	
	 
	
Example 1:
	
	Input: nums = [1,2,3,4]
	
	Output: 3
	
	Explanation:
	
	All array elements can be made divisible by 3 using 3 operations:
	
	Subtract 1 from 1.
	Add 1 to 2.
	Subtract 1 from 4.
 
Example 2:
	
	Input: nums = [3,6,9]
	
	Output: 0
	
	 
	
Constraints:
	
	1 <= nums.length <= 50
	1 <= nums[i] <= 50
 

```java
class Solution {
    private boolean check(int n){
        if(n % 3 == 0){
            return true;
        }
        return false;
    }


    public int minimumOperations(int[] nums) {
        int operationCounter = 0;
        for(int i : nums){
            if(i % 3 != 0){
                // check sub
                boolean subSuccess = check(i-1);
                if(subSuccess){
                    operationCounter++;
                    continue;
                }
                boolean addSuccess = check(i+1);
                if(addSuccess){
                    operationCounter++;
                }
                
            }
        }
        return operationCounter;
        
    }
}

// Hint: If x % 3 != 0 we can always increment or decrement x such that we only need 1 operation.

        public int minimumOperations(int[] nums) {
        int operationCounter = 0;
        for(int i : nums){
            if(i % 3 != 0){
                operationCounter++;
                
            }
        }
        return operationCounter;
        
    }

```
---

## 2011. Final Value of Variable After Performing Operations - Easy

	There is a programming language with only four operations and one variable X:
	
	++X and X++ increments the value of the variable X by 1.
	--X and X-- decrements the value of the variable X by 1.
	Initially, the value of X is 0.
	
	Given an array of strings operations containing a list of operations,
 	return the final value of X after performing all the operations.

```java
class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for(String operation : operations){
            if(operation.equals("X++") || operation.equals("++X")){
                x++;
            }else{
                x--;
            }
        }
        return x;
        
    }
}
```




---

## 1929. Concatenation of Array - Easy

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

class Solution {
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




// another way

int[] originalArray = {3, 6, 9, 10};

int[] result = new int[originalArray.length * 2]; // [0, 0, 0, 0, 0, 0, 0, 0]

// copy first
for(int i=0; i < originalArray.length; i++){
    result[i] = originalArray[i];
}

// copy the rest

System.arraycopy(originalArray, 0, result, originalArray.length, originalArray.length);

System.out.println(Arrays.toString(result)); // [3, 6, 9, 10, 3, 6, 9, 10]

     

```

---

## 1920. Build Array from Permutation - Easy

    Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

    A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

 

Example 1:

    Input: nums = [0,2,1,5,3,4]

    Output: [0,1,2,4,5,3]

    Explanation: The array ans is built as follows: 
    ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
        = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
        = [0,1,2,4,5,3]

Example 2:

    Input: nums = [5,0,1,2,3,4]
    Output: [4,5,0,1,2,3]
    Explanation: The array ans is built as follows:
    ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
        = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
        = [4,5,0,1,2,3]
 

Constraints:

    1 <= nums.length <= 1000
    0 <= nums[i] < nums.length
    The elements in nums are distinct.
 

Follow-up

    Can you solve it without using an extra space (i.e., O(1) memory)?

```java

class Solution {
    public int[] buildArray(int[] nums) {
        int nums_length = nums.length;

        int[] result = new int[nums_length];

        for (int i = 0; i < nums_length; i++) {
            result[i] = nums[nums[i]];
        }

        return result;
    }
}


// follow up - without using an extra space

/*
At every point we need to keep track of "these values"

	a = nums[i]
	b = nums[a] or nums[nums[i]]

Look at the constraints,
we can use the other bits to
store information

If we were dealing with strings -> we could append "these values" with a separator

Since we are dealing with int, "appending / adding "these value", we go beyond the constraints

Note:

	our_meta_information = meta_data = num1 + (some_constant)*num2

	meta_data = num1 + (some_constant)*num2

     
	>> nums1 and nums2 === can either be the "a", or "b"
	>> some_constant  ===  a very large number beyond the num values / prime number / bounds of the array

		
How can we recover the data:

	num1 = meta_data % (some_constant)
	
	num2 = meta_data / (some_constant)

	

Note:
- You will need the original value in the computation,
- that is where the recovery data comes from



*/

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


```

---

## 1512. Number of Good Pairs- Easy

    Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: Each pair in the array are good.

Example 3:

    Input: nums = [1,2,3]
    Output: 0
 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100

```java

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numIdenticalPairs(int[] nums) {

        HashMap<Integer, Integer> myHashMap = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (myHashMap.containsKey(nums[i])) {
                myHashMap.put(nums[i], myHashMap.get(nums[i]) + 1);
            }else{
                myHashMap.put(nums[i], 1);
            }
                
        }

        // compute the good pairs (n * (n-1))/2
        int result = 0;
        for(Map.Entry<Integer, Integer> entry : myHashMap.entrySet()){
            if(entry.getValue() > 1){
                result = result + ((entry.getValue() * (entry.getValue()-1))/2);
            }
        }

        return result;

    }
}

// Handshake in gathering -> idea

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

```








