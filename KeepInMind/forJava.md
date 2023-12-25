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
