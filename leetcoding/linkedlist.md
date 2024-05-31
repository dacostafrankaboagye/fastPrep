## 705. Design HashSet
        
        Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:
        
        Input
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
        [[], [1], [2], [1], [3], [2], [2], [2], [2]]
        Output
        [null, null, null, true, false, null, true, null, false]
        

Explanation

        MyHashSet myHashSet = new MyHashSet();
        myHashSet.add(1);      // set = [1]
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(1); // return True
        myHashSet.contains(3); // return False, (not found)
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(2); // return True
        myHashSet.remove(2);   // set = [1]
        myHashSet.contains(2); // return False, (already removed)

 

Constraints:
        
        0 <= key <= 106
        At most 104 calls will be made to add, remove, and contains.


```java


class Node{
    public int data;
    private Node next;

    Node(int data){
        this.data = data;
        this.next = null;
    }

    public Node getNextNode(){
        return this.next;
    }

    public void setNextNode(Node node){
        this.next = node;
    }

}

class SLinkedList{

    public Node head;

    SLinkedList(){
        this.head = null;
    }

    public void addToHead(int data){
        Node newHead = new Node(data);
        Node currentHead = this.head;
        this.head = newHead;
        if(currentHead != null){
            this.head.setNextNode(currentHead);
        }
    }

    // adding to the end
    public void addToTail(int data){
        Node newTail = new Node(data);
        Node currentTail = this.head;
        if(currentTail != null){
            while(currentTail.getNextNode() != null){
                currentTail = currentTail.getNextNode();
            }
            currentTail.setNextNode(newTail);
        }else{
            this.head = newTail;
        }
    }

    public boolean dataInList(int data){
        Node currentHead = this.head;
        while(currentHead != null){
            if(currentHead.data == data){
                return true;
            }
            currentHead = currentHead.getNextNode();
        }
        return false;
    }

    public int removeHead(){
        Node currentHead = this.head;
        if(currentHead == null){return -1;}  // we return -1 to show that the head isn't there
        this.head = currentHead.getNextNode();
        return currentHead.data;
    }

    public int removeData(int data){
        Node currentHead = this.head;
        Node previous = this.head;
        while(currentHead != null){
            if(currentHead.data == data){
                // if it is the head - remove head
                // if it is the tail - remove tail
                // otherwise - do your operation

                if(currentHead == this.head){return removeHead();}
                else{
                    previous.setNextNode(currentHead.getNextNode());
                    return currentHead.data;
                }
                
            }
            previous = currentHead;
            currentHead = currentHead.getNextNode();
            

        }
        return -1;
    }

    public void printOut(){
        Node currrentHead = this.head;
        System.out.println("\n");
        System.out.print("<Head> ");
        while(currrentHead != null){
            System.out.print(currrentHead.data + " ");
            currrentHead = currrentHead.getNextNode();
        }
        System.out.println(" <Tail>");
        System.out.println("\n");
    }

}

class MyHashSet {
    SLinkedList myLinkedList;

    public MyHashSet() {
        myLinkedList = new SLinkedList();
        
    }
    
    public void add(int key) {
        if(!myLinkedList.dataInList(key)){
            myLinkedList.addToTail(key);
        }
        
    }
    
    public void remove(int key) {
        myLinkedList.removeData(key);

        
    }
    
    public boolean contains(int key) {
        return myLinkedList.dataInList(key);   
    }

    public void show(){
        myLinkedList.printOut();
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
```


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
