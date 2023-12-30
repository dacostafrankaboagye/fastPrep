## Printing

```java

myStack.forEach(element -> System.out.println(element));


Iterator<Integer> iterator = stack.iterator();
while (iterator.hasNext()) {
    System.out.print(iterator.next() + " ");
}


// s1, s2, s3 could be different things
for(Object i : new Object[]{s1, s2, s3}){
    System.out.println(i);
}



// Using Java Streams
Arrays.stream(myIntArray).forEach(num -> System.out.print(num + " "));



// Using Arrays.toString() method - more readable and conise
System.out.println(Arrays.toString(myIntArray));



```

## initialising 
```java

List<Integer> integerList = Arrays.asList(1, 2, 3, 4, 5);

```

## Summing
```java
List<Integer> myList = Arrays.asList(1, 2, 3, 4, 5);
int sum = myList.stream().reduce(0, Integer::sum);
```

## Sorting
```java

int[] numbers = {5, 2, 9, 1, 5, 6};
Arrays.sort(numbers);


```
