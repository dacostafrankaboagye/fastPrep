/*
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

Sample Input
STDIN       Function
-----       --------
5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4  
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]

Sample Output
5
*/

/*

 - To find the solution we need to maximize this height and that should be the answer to this problem.
 - We can create 3 new stacks with the cumulative sums of the cylinder heights in each stack. 
 - This way the top element of each stack would tell you the current height of the stack
 - go on removing the highest element from each of the 3 stacks until the top element of all the stacks is same.
*/





class Result {

    /*
     * Complete the 'equalStacks' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
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


