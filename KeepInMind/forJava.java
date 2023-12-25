/*
printing elements in a stack
*/

myStack.forEach(element -> System.out.println(element));

Iterator<Integer> iterator = stack.iterator();
while (iterator.hasNext()) {
    System.out.print(iterator.next() + " ");
}

