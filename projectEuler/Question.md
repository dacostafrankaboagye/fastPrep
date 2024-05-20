
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

The sum of the squares of the first ten natural numbers is,

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <msup>
    <mn>1</mn>
    <mn>2</mn>
  </msup>
  <mo>+</mo>
  <msup>
    <mn>2</mn>
    <mn>2</mn>
  </msup>
  <mo>+</mo>
  <mo>.</mo>
  <mo>.</mo>
  <mo>.</mo>
  <mo>+</mo>
  <msup>
    <mn>10</mn>
    <mn>2</mn>
  </msup>
  <mo>=</mo>
  <mn>385.</mn>
</math>





