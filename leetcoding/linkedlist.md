
## 1290. Convert Binary Number in a Linked List to Integer

    Given head which is a reference node to a singly-linked list. 
    
    The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
    
    Return the decimal value of the number in the linked list.
    
    The most significant bit is at the head of the linked list.
    
    Example 1:
    
    
    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10
    Example 2:
    
    Input: head = [0]
    Output: 0
     
    
    Constraints:
    
    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.


```java

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {

        String a = "";
        ListNode current = head;
        while(current != null){
            a += current.val;
            current = current.next;
        }
        int decimalForm = Integer.parseInt(a, 2);
        

        return decimalForm;
        
    }
}


//---------- or

class Solution {
    public int getDecimalValue(ListNode head) {

        ListNode current = head;
        int result = 0;

        while(current != null){
            result  = result << 1;
            if(current.val == 1){
                result = result | 1;
            }
            current = current.next;
        }

        return result;
        
    }
}

```


## 876. Middle of the Linked List

        Given the head of a singly linked list, return the middle node of the linked list.
        
        If there are two middle nodes, return the second middle node.
        
         
        
        Example 1:
        
        
        Input: head = [1,2,3,4,5]
        Output: [3,4,5]
        Explanation: The middle node of the list is node 3.

        
        Example 2:
        
        
        Input: head = [1,2,3,4,5,6]
        Output: [4,5,6]
        Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
         
        
        Constraints:
        
        The number of nodes in the list is in the range [1, 100].
        1 <= Node.val <= 100


```java

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null){
            fast = fast.next;
            if(fast != null){
                fast = fast.next;
                slow = slow.next;
            }
        }

        return slow;
        
    }
}

```
