

## Special Pythagorean Triplet - Problem 9


```java

```



## 10001st Prime - Problem 7

<p>By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.</p>

<p>What is the 10,001st prime number?</p>

        Answer:  104743
        
```java

static boolean isPrime(int n){
        if(n <= 1){
            return false;
        }
        for(int i=2; i<=Math.sqrt(n); i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;
}

static int nthPrime(int n){
        // n cannot be <= 0
        int number = 2;
        int primeCounter = 0;
        while(primeCounter < n){
            if(isPrime(number)){
                primeCounter += 1;
            }
            number += 1;
        }
        return number - 1;
}

```

---

## Largest Palindrome Product - Problem 4
        
A palindromic number reads the same both ways. 

The largest palindrome made from the product of 

two 2-digit numbers is 9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.


        Answer:  906609


```java

static boolean isPalindrome(int prod){
    String s = Integer.toString(prod);
    return s.equals(new StringBuilder(s).reverse().toString());
}

static int largestPalindromicProduct(){
    int maxPalindrome = 0;
    for(int i=100; i< 1000; i++){
        for(int j=100; j<1000; j++){
            int prod = i*j;
            if(isPalindrome(prod)){
                maxPalindrome = Math.max(maxPalindrome, prod);
            }
        }
    }

    return maxPalindrome;
}

```

---

## Largest Prime Factor
  The prime factors of $13195$ are 5, 7, 13 and 29
  
  What is the largest prime factor of the number 600851475143
  


    Ans: 6857

```java
    static BigInteger largestPrimeFactors(BigInteger n){

        BigInteger largest = BigInteger.valueOf(-1);

        for(BigInteger d = BigInteger.valueOf(2); d.compareTo(n) < 0; d = d.add(BigInteger.ONE) ){

            while(n.mod(d).equals(BigInteger.ZERO)){
                n = n.divide(d);
                largest = largest.max(d);

            }
        }
        if(!n.equals(BigInteger.ONE)){
            largest = largest.max(n);
        }

        System.out.println("Largest : " + largest);


        return largest;
    }
```

## Sum Square Difference

  The sum of the squares of the first ten natural numbers is,
  1^2 + 2^2 + ... + 10^2 = 385.
  
  The square of the sum of the first ten natural numbers is,
  (1 + 2 + ... + 10)^2 = 55^2 = 3025.
    
  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
  
  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
  
  
    Ans: 25164150

```java


    static double sumSquareDifference(int n){
        // square of the sum of the first n  natural numbers
        double sumOf_N_NaturalNumber = (n * (n + 1)) / 2;
        double squareOfThe_sumOf_N_NaturalNumber = Math.pow(sumOf_N_NaturalNumber, 2);

        // sum of the squares of the first n natural numbers
        double sumOfTheSquaresOf_N_NaturalNumbers = ( n*(n+1)*( (2*n) + 1) ) / 6;

        return squareOfThe_sumOf_N_NaturalNumber - sumOfTheSquaresOf_N_NaturalNumbers;

    }
```


## Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1  to 10  without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1  to 20 ?


    Ans : 232792560





```java

//-------------------------solution - 1

static boolean canBeDividedFrom1to20(int n){
    for(int i=1; i<=20; i++){
        if(n%i != 0){
            return false;
        }
    }
    return true;
}

int smallestNumber = 1;

while(true){
    if(canBeDividedFrom1to20(smallestNumber)){
        break;
    }
    smallestNumber +=1;
}

System.out.println("\nnumber: " + smallestNumber);

//---------------------------------------------



/*


// can we make it better

-> the nnumber we are checking needs to be divisible by 1
    -> but all numbers are divisible by 1
    -> the range then goes from
       from:  range(1, 20)
        to:   range(2, 20)

        // 1st modification -- we start i at "2"
        for(int i=2; i<=20; i++){
            if(n%i != 0){
                return false;
            }
        }
        return true;
    

    What then does this mean?
    -> for every number we check if that number is divisble by all numbers from 2, to 20
    -> Note: from 2, to 20
    -> meaning that if the number should be divisible by / starting at 2: then the number should be an even number right?

    // 2nd Modification -- we start searching for the number from "2" to infinity
        -> perform an increment of / by 2
        // so we do not vene check the odd numbers
    
        int smallestNumber = 2;
        while(true){
            if(canBeDividedFrom1to20(smallestNumber)){
                break;
            }
            smallestNumber +=2;
        }


    // lets think about it a little more
    // the number should be divisible by all numbers from 1 to 20
    we have already dealt with "1"
    so the number should be divisible by all numbers from 2 to 20
        // if it divisible by 2... that mean all the even numbers will be valid

    // think of this .. 20 is part
    // so the number should be divisible by 20 too...

    // so we start searching for the number at 20
    // and keep incrementing it by 20

    // so we will end up checking 20, 40, 50, 60, .. up to the time we find the number [that can be divisible by all numbers from 2 to 20]

*/


static boolean canBeDividedFrom1to20(int n){
    for(int i=2; i<=20; i++){
        if(n%i != 0){
            return false;
        }
    }
    return true;
}

int smallestNumber = 20;

while(true){
    if(canBeDividedFrom1to20(smallestNumber)){
        break;
    }
    smallestNumber +=20;
}

```

---


# Helpers

---

### GCD
```java

// greatest common divisor (GCD) of two numbers using the Euclidean algorithm

  public static int gcd(int a, int b) {
      // Base case: If b is 0, then GCD is a
      if (b == 0) {
          return a;
      }
      // Recursive case: Compute GCD of b and a mod b
      return gcd(b, a % b);
  }

```

### LCM

```java

// find the LCM (Least Common Multiple) of two numbers

    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }
    
```



















