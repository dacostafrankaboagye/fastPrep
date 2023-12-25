## Question
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. 
You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
This means you must remove zero or more cylinders from the top of zero or more of the three stacks 
until they are all the same height, then return the height.

Example
h1 = [1,2,1,1]
h2 = [1,1,2]
h3 = [1,1]


There are 4, 3, and 2 cylinders in the three stacks, with their heights in the three arrays.
Remove the top 2 cylinders from h1 (heights = [1, 2]) and from h2 (heights = [1, 1]) 
so that the three stacks all are 2 units tall. Return 2 as the answer.

Note: An empty stack is still a stack.


You have three stacks of cylinders where each cylinder has the same diameter,
but they may vary in height. You can change the height of a stack by removing
and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are
exactly the same height. This means you must remove zero or more cylinders from the
top of zero or more of the three stacks until they are all the same height, then return the height.


Example

There are  and  cylinders in the three stacks, with their heights in the three arrays. 
Remove the top 2 cylinders from  (heights = [1, 2]) and from  (heights = [1, 1]) 
so that the three stacks all are 2 units tall. Return  as the answer.

Note: An empty stack is still a stack.

Function Description

Complete the equalStacks function in the editor below.

equalStacks has the following parameters:

int h1[n1]: the first array of heights
int h2[n2]: the second array of heights
int h3[n3]: the third array of heights

Returns
int: the height of the stacks when they are equalized
```
Sample Input
STDIN       Function
-----       --------
5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4  
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]
```
Sample Output
5


## Approach - 1
  - To find the solution we need to maximize this height and that should be the answer to this problem.
  - We can create 3 new stacks with the cumulative sums of the cylinder heights in each stack. 
  - This way the top element of each stack would tell you the current height of the stack
  - go on removing the highest element from each of the 3 stacks until the top element of all the stacks is same.

## Approach - 2
  - Find the sum of elements in each stack
  - while there are still values in the stack
    - we find the minimum of the sum of the stack
    - while the minimum is less than the sum of each of the stack
    - we subtract from the sum and pop that value out and update the sum
    - we do this for the three sums.
  - if the sum of the first stack == sum of the second stack == sum of the third stack : we have our ans and break / return
  - else: continue the main loop
  - return 0 : when it come out of the main loop : 

## Solution - 1
  
  ### Java
  ```java
  class Result {
  
      /*
       * Complete the 'equalStacks' function below.
       *
       * The function is expected to return an INTEGER.
       * The function accepts the following parameters:
       *  1. INTEGER_ARRAY h1
       *  2. INTEGER_ARRAY h2
       *  3. INTEGER_ARRAY h3
       */
  
      public static void fillStack(Stack<Integer> stack1, List<Integer> h1, Stack<Integer> stack2, List<Integer> h2, Stack<Integer> stack3, List<Integer> h3){
          int stackSum = 0;
  
          for(int i=h1.size()-1; i >=0; i--){
              stackSum += h1.get(i);
              stack1.push(stackSum);
          }
          stackSum = 0;
          for(int i=h2.size()-1; i >=0; i--){
              stackSum += h2.get(i);
              stack2.push(stackSum);
          }
          stackSum = 0;
          for(int i=h3.size()-1; i >=0; i--){
              stackSum += h3.get(i);
              stack3.push(stackSum);
          }
      }
  
  
      public static int equalStacks(List<Integer> h1, List<Integer> h2, List<Integer> h3) {
          // create new stacks
          // fill those stacks with the cumulative sum
          // identify the largest value in the stack and pop it out
              // do this till the values in the stack are equal
  
          int maxHeight = 0;
  
          Stack<Integer> stack1 = new Stack<>();
          Stack<Integer> stack2 = new Stack<>();
          Stack<Integer> stack3 = new Stack<>();
  
          fillStack(stack1, h1, stack2, h2, stack3, h3);
  
          while(!stack1.isEmpty() && !stack2.isEmpty() && !stack3.isEmpty()){
  
              int stack1Value = stack1.peek();
              int stack2Value = stack2.peek();
              int stack3Value = stack3.peek();
  
              if(stack1Value == stack2Value && stack1Value == stack3Value){
                  maxHeight = stack1.pop();
                  break;
              }
  
              if(stack1Value >= stack2Value && stack1Value >= stack3Value){
                  stack1.pop();
              }
              else if(stack2Value >= stack1Value && stack2Value >= stack3Value){
                  stack2.pop();
              }
              else if(stack3Value >= stack1Value && stack3Value >= stack2Value){
                  stack3.pop();
              }
          }
  
          return maxHeight;
      }
  }
  ```
  ### Python
  ```py
  # Equivalent Python code from the Java solution
  def fillStack(myStack, h):
      stackSum = 0
      for i in range(len(h)-1, -1, -1):
          stackSum += h[i]
          myStack.append(stackSum)
          
      
  def equalStacks(h1, h2, h3):
      # Write your code here
      maxHeight = 0
      stack1 = []
      stack2 = []
      stack3 = []
      
      fillStack(stack1, h1)
      fillStack(stack2, h2)
      fillStack(stack3, h3)
      
      while len(stack1) != 0 and len(stack2) != 0 and len(stack3)!=0:
          stack1Value = stack1[-1]
          stack2Value = stack2[-1]
          stack3Value = stack3[-1]
          if stack1Value == stack2Value == stack3Value:
              maxHeight = stack1.pop()
              break
          if stack1Value >= stack2Value and stack1Value >= stack3Value:
              stack1.pop() 
          elif stack2Value >= stack1Value and stack2Value >= stack3Value:
              stack2.pop() 
          elif stack3Value >= stack1Value and stack3Value >= stack2Value:
              stack3.pop() 
      return maxHeight
  
  # Another version of the code above 
  def fill_stack(my_stack, h):
      stack_sum = 0
      for height in reversed(h):
          stack_sum += height
          my_stack.append(stack_sum)
  
  def equalStacks(h1, h2, h3):
      stack1, stack2, stack3 = [], [], []
      
      fill_stack(stack1, h1)
      fill_stack(stack2, h2)
      fill_stack(stack3, h3)
  
      while stack1 and stack2 and stack3:
          max_height = min(stack1[-1], stack2[-1], stack3[-1])
          while stack1 and stack1[-1] > max_height:
              stack1.pop()
          while stack2 and stack2[-1] > max_height:
              stack2.pop()
          while stack3 and stack3[-1] > max_height:
              stack3.pop()
  
          if stack1 and stack2 and stack3 and stack1[-1] == stack2[-1] == stack3[-1]:
              return stack1[-1]
  
      return 0
  ```
## Solution 2
  
  ### Python
  ```py
  def equalStacks(h1, h2, h3):
      s1 = sum(h1)
      s2 = sum(h2)
      s3 = sum(h3)
      
      while h1 and h2 and h3:
          m = min(s1, s2, s3)
          while s1 > m:
              s1 = s1 - h1.pop(0)
          while s2 > m:
              s2 = s2 - h2.pop(0)
          while s3 > m:
              s3 = s3 - h3.pop(0)
          
          if s1 == s2 == s3:
              return s1 
      return 0
  ```

### Java
```java
class Result {

    public static void fillStack(Stack<Integer> stack1, List<Integer> h1){
        int stackSum = 0;
        for(int i=h1.size()-1; i >=0; i--){
            stackSum = h1.get(i);
            stack1.push(stackSum);
        }
    }
    public static int mySum(List<Integer> myList){
        int result = 0;
        for(int i : myList){
            result += i;
        }
        return result;
    }


    public static int equalStacks(List<Integer> h1, List<Integer> h2, List<Integer> h3) {

        int s1 = mySum(h1);
        int s2 = mySum(h2);
        int s3 = mySum(h3);

        Stack<Integer> st1 = new Stack<>();
        Stack<Integer> st2 = new Stack<>();
        Stack<Integer> st3 = new Stack<>();

        fillStack(st1, h1);
        fillStack(st2, h2);
        fillStack(st3, h3);

        while(!st1.isEmpty() && !st2.isEmpty() && !st3.isEmpty()){

            int m = Math.min(s1, Math.min(s2, s3));

            while(s1 > m){
                s1 = s1 - st1.pop();
            }
            while(s2 > m){
                s2 = s2 - st2.pop();
            }
            while(s3 > m){
                s3 = s3 - st3.pop();
            }
            if(s1 == s2 && s1 == s3){
                return s1;
            }
        }

        return 0;

    }

}
```
