
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
  <p>The square of the sum of the first ten natural numbers is,
  (1 + 2 + ... + 10)^2 = 55^2 = 3025.
  <p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
  <p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
  
  
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





