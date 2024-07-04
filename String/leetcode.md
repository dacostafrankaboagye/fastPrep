
# General


---


## 3146. Permutation Difference between Two Strings - Easy
	
	You are given two strings s and t such that every character occurs 
 
 	at most once in s and t is a permutation of s.
	
	The permutation difference between s and t is defined as the sum of the 
 
 	absolute difference between the index of the occurrence of 
  	
   	each character in s and the index of the occurrence of the same character in t.
	
	Return the permutation difference between s and t.

 

Example 1:

	Input: s = "abc", t = "bac"
	
	Output: 2
	
	Explanation:
	
	For s = "abc" and t = "bac", the permutation 
 
 	difference of s and t is equal to the sum of:
	
	The absolute difference between the index of the  
 	occurrence of "a" in s and the index of the occurrence of "a" in t.
  
	The absolute difference between the index of the occurrence of 
 	"b" in s and the index of the occurrence of "b" in t.
  
	The absolute difference between the index of the 
 	occurrence of "c" in s and the index of the occurrence of "c" in t.
  
	That is, the permutation difference between 
 	s and t is equal to |0 - 1| + |2 - 2| + |1 - 0| = 2.

Example 2:

	Input: s = "abcde", t = "edbac"
	
	Output: 12
	
	Explanation: The permutation difference between s and t is 
 	equal to |0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12.

 

Constraints:
	
	1 <= s.length <= 26
	Each character occurs at most once in s.
	t is a permutation of s.
	s consists only of lowercase English letters.

```java

class Solution {
    public int findPermutationDifference(String s, String t) {
        int result = 0;
        for(int i=0; i<s.length(); i++){
            result += Math.abs(i - t.indexOf(s.charAt(i)));
        }
        return result;
        
    }
}

```

---

## 3110. Score of a String Easy

	You are given a string s. The score of a string is 
 	defined as the sum of the absolute difference between 
  	the ASCII values of adjacent characters.
	
	Return the score of s.

 

Example 1:

	Input: s = "hello"
	
	Output: 13
	
	Explanation:
	
	The ASCII values of the characters in s 
 	are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. 
  
  	So, the score of s would be 
   
   	|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| 
   
	= 3 + 7 + 0 + 3 = 13.

Example 2:

	Input: s = "zaz"
	
	Output: 50

	Explanation:
	
	The ASCII values of the characters in s are: 
 
 	'z' = 122, 'a' = 97. So, the score of s would be 
  
  	|122 - 97| + |97 - 122| = 25 + 25 = 50.

 

Constraints:
	
	2 <= s.length <= 100
	s consists only of lowercase English letters.


```java
class Solution {
    public int scoreOfString(String s) {
        int result = 0;
        for(int i=0; i< s.length()-1; i++){
            result += Math.abs(s.charAt(i) - s.charAt(i+1));
        }
        return result;
        
    }
}
```

---

## 1108. Defanging an IP Address - Easy

Given a valid (IPv4) IP address, return a defanged version of that IP address.

        A defanged IP address replaces every period "." with "[.]".

 

Example 1:

        Input: address = "1.1.1.1"
        Output: "1[.]1[.]1[.]1"

Example 2:

        Input: address = "255.100.50.0"
        Output: "255[.]100[.]50[.]0"
        

Constraints:

        The given address is a valid IPv4 address.


### solution - python
```py

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

        
# Test cases
def test_defangIPaddr():
    solution = Solution()

    # Example 1
    input_1 = "1.1.1.1"
    expected_output_1 = "1[.]1[.]1[.]1"
    assert solution.defangIPaddr(input_1) == expected_output_1

    # Example 2
    input_2 = "255.100.50.0"
    expected_output_2 = "255[.]100[.]50[.]0"
    assert solution.defangIPaddr(input_2) == expected_output_2

    print("All test cases passed!")

# Run the test
test_defangIPaddr()

```
---

## 1678. Goal Parser Interpretation - Easy

You own a Goal Parser that can interpret a string command. 

The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 

The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 

The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

        Input: command = "G()(al)"
        Output: "Goal"
        
Explanation: The Goal Parser interprets the command as follows:

        G -> G
        () -> o
        (al) -> al

        The final concatenated result is "Goal".

Example 2:

        Input: command = "G()()()()(al)"
        Output: "Gooooal"

Example 3:

        Input: command = "(al)G(al)()()G"
        Output: "alGalooG"
        

Constraints:

        1 <= command.length <= 100
        command consists of "G", "()", and/or "(al)" in some order.

### solution - python
```py
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)", "al").replace("()", "o")
        
```
