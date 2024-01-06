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

---

## 876. Middle of the Linked List - Easy

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

    public static int getNodeLength(ListNode head) {
        ListNode current = head;
        int ans = 0;
        while (current != null ) {
            ans += 1;
            current = current.next;
        }
        return ans;
    }
    
    public ListNode middleNode(ListNode head) {

        int nodelegth = getNodeLength(head);
        int midVal = nodelegth / 2;
        ListNode current = head;
        int index = 0;
        while(current != null && index < midVal){
            current = current.next;
            index += 1;
        }
        return current;
    }



    // bette solution
    // clever
    public static int middleNode(ListNode head) {

        ListNode temp = head;
        
        while(temp != null && temp.next != null){
            head = head.next;
            temp = temp.next.next;            
        }
        return head.val;


    }

}


```

### solution - python
```py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def nodeLength(self, head):
        ans = 0
        while head:
            head = head.next
            ans +=1
        return ans

    def middleNode_old(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodelen = self.nodeLength(head)
        middleValue = nodelen // 2
        index = 0
        current = head
        while current and (index < middleValue):
            current = current.next
            index += 1
        return current

    
    # clever way
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp =head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next 
        return head
        

        
        
```

---

## 206. Reverse Linked List - Easy

    Given the head of a singly linked list, reverse the list, and return the reversed list.

    

    Example 1:


        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]


    Example 2:


        Input: head = [1,2]
        Output: [2,1]


    Example 3:

        Input: head = []
        Output: []
    

    Constraints:

        The number of nodes in the list is the range [0, 5000].
        -5000 <= Node.val <= 5000
    

    Follow up
        A linked list can be reversed either iteratively or recursively. Could you implement both?

### solution - python
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
current = head
prev = current 

temp = current.next
current.next = prev
prev = current
current = temp

'''

class Solution:
    def reverseList_one(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp 
        return previous
        
    # recurssive

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseList_recurssive(head, previous=None)

    def reverseList_recurssive(self, head, previous=None):
        if head is None:
            return previous

        temp = head.next
        head.next = previous
        # previous = head
        # head = temp
        '''
        or return reverseList_recurssive(head=temp, prevoius=head)
        and remove the variables
        ''' 

        return self.reverseList_recurssive(head=temp, previous=head)
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
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode prev = null;
        while(current != null) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }

    public static ListNode reverseList_recurssive(ListNode head, ListNode previous) {
        if(head == null){
            return previous;
        }
        ListNode next = head.next;
        head.next = previous;
        return reverseList_recurssive(next, head);
    }


}

```