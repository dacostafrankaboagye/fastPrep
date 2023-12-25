## Printing elements in a stack

```java 
myStack.forEach(element -> System.out.println(element));

Iterator<Integer> iterator = stack.iterator();
while (iterator.hasNext()) {
    System.out.print(iterator.next() + " ");
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
