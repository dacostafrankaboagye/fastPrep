/* printing elements in a stack */

myStack.forEach(element -> System.out.println(element));

Iterator<Integer> iterator = stack.iterator();
while (iterator.hasNext()) {
    System.out.print(iterator.next() + " ");
}


/* initialising */

List<Integer> integerList = Arrays.asList(1, 2, 3, 4, 5);
