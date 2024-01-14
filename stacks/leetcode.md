
## 1021. Remove Outermost Parentheses - Esay
    (tags: string, stack)

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example,

     "", "()", "(())()", and "(()(()))" 
     
are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into 

        s = A + B

 with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

        Input: s = "(()())(())"
        Output: "()()()"
        Explanation: 
        The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
        After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

        Input: s = "(()())(())(()(()))"
        Output: "()()()()(())"
        Explanation: 
        The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
        After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

        Input: s = "()()"
        Output: ""
        Explanation: 
        The input string is "()()", with primitive decomposition "()" + "()".
        After removing outer parentheses of each part, this is "" + "" = "".
 

Constraints:

        1 <= s.length <= 105
        s[i] is either '(' or ')'.
        s is a valid parentheses string.

### solution - python
```py
class Solution:
    # approach 1 
    def removeOuterParentheses_1(self, s: str):
        openCout = 0
        temp = result = ""
        result = ""
        for c in s:
            if c == '(':
                openCout +=1 
            else:
                openCout -=1
            temp += c
            if openCout == 0:
                result += temp[1:-1]
                temp = ""
        return result 

    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        stack = []

        for char in s:
            if char == '(':
                if stack:
                    result += char
                stack.append(char)
            else:
                stack.pop()
                if stack:
                    result += char

        return result

```

### solution - java
```java

```

## 1614. Maximum Nesting Depth of the Parentheses - Easy

A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
Example 2:

Input: s = "(1)+((2))+(((3)))"
Output: 3
 

Constraints:

1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.

### solution - python
```py
class Solution:
    def maxDepth(self, s: str) -> int:
        myStack = []
        maxSize = 0
        for s in s:
            if s is '(':
                myStack.append(s)
                maxSize = max(maxSize, len(myStack))
            elif s is ')':
                if myStack:
                    myStack.pop()

        return maxSize
```