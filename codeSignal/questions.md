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


```
