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