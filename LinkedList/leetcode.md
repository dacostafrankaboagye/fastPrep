## 1290. Convert Binary Number in a Linked List to Integer - Easy

  Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
  
  
  The linked list holds the binary representation of a number.
  
  
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

  ### solution - python
  ```py
  
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  
  class Solution:
      
      def getDecimalValue1(self, head: ListNode) -> int:
          current = head
          strAns = '0b'
          while current is not None:
              strAns += str(current.val)
              current = current.next
          return int(strAns, base=0)
      
      # another way
      def getDecimalValue(self, head: ListNode) -> int:
          ans = 0
          while head:
              ans = (2 * ans) + head.val
              head = head.next
          return ans
  
  ```

### solution - java
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
    
    public int getDecimalValue1(ListNode head) {
        ListNode current = head;
        String strAns = "";
        while(current != null){
            strAns = strAns + Integer.toString(current.val);
            current = current.next;
        }
        return Integer.parseInt(strAns, 2);
        
    }

    /*
    the other solution
    */


    public int getDecimalValue(ListNode head) {
        ListNode current = head;
        int ans = 0;
        while(current != null){
            ans = (ans * 2 )+ current.val;
            current = current.next;
        }
        return ans;
        
    }


}

```
