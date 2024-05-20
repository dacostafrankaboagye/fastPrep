
## Largest Prime Factor
<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>

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

<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>






