## century
    Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
  Example
    
    For year = 1905, the output should be
    solution(year) = 20;
    For year = 1700, the output should be
    solution(year) = 17.

```java

int solution(int year) {
    
    if(year <= 100){
        return 1;
    }
    int result = year / 100;
    if (year % 100 > 0){
        result += 1;
    }
    return result;

}

```

## check palindrome

    Given the string, check if it is a palindrome.

    A string that doesn't change when reversed (it reads the same backward and forward).

  Examples:
      
      "eye" is a palindrome
      "noon" is a palindrome
      "decaf faced" is a palindrome
      "taco cat" is not a palindrome (backwards it spells "tac ocat")
      "racecars" is not a palindrome (backwards it spells "sracecar")
    
  Example
      
      For inputString = "aabaa", the output should be
      solution(inputString) = true;
      For inputString = "abac", the output should be
      solution(inputString) = false;
      For inputString = "a", the output should be
      solution(inputString) = true.
    
```java
static String reverseString(String theString){
    StringBuilder sb = new StringBuilder();
    for(int i=theString.length()-1; i >=0; i--){
        sb.append(theString.charAt(i));
    }
    return sb.toString();
}

boolean solution(String inputString) {
    return inputString.equals(reverseString(inputString));

}


```
---

## adjacentElementsProduct

    Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

    For inputArray = [3, 6, -2, -5, 7, 3], the output should be
    solution(inputArray) = 21.

    7 and 3 produce the largest product.

Input/Output

    [execution time limit] 3 seconds (java)

    [memory limit] 1 GB

    [input] array.integer inputArray

An array of integers containing at least two elements.

    Guaranteed constraints:
    2 ≤ inputArray.length ≤ 10,
    -1000 ≤ inputArray[i] ≤ 1000.

    [output] integer

    The largest product of adjacent elements.

```java



int solution(int[] inputArray) {
    int result = -2147483648;
    for(int i=1; i<inputArray.length; i++){
        int product = inputArray[i] * inputArray[i-1];
        result = Math.max(result, product);
    }
    return result;

}


```








