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

---

## 705. Design HashSet - Easy

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

### solution - py
```py
'''
my hashset

index | linkedlist (the actaul key)
0      1 -> 2 -> 3 -> 4 -> NULL
1
2
.
.
.
9999

because : 10^4 calls can be made
hash function
    - key % len(hashset)

    with this I can have say::
    if key = 10001 then % 10000 = 1
    if key = 20001 then % 10000 = 1
    if key = 30001 then % 10000 = 1
    if key = 2 then % 10000 = 2
    if key = 10002 then % 10000 = 2
    
    now if I added all those keys to the hashset
        index | linkedlist (the actaul key)
        0      
        1       10001 -> 20001 -> 30001 -> Null
        2        2 -> 10002 -> Null
        .
        .
        .
        9999

    
        all will be at the same index but different values - reason for the linkedlist


        
    
'''
class ListNode:
    
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        # creating a dummy node for the fixed sized calls we have
        self.myHashSet = [ListNode(0) for i in range(10000)]
      

    def _hashFunction(self, key):
        return key % len(self.myHashSet)

    def add(self, key: int) -> None:
        index = self._hashFunction(key)
        current = self.myHashSet[index]
        while current.next:
            if current.next.key == key:
                return
            current = current.next
        current.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        index = self._hashFunction(key)
        current = self.myHashSet[index]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        
    def contains(self, key: int) -> bool:
        index = self._hashFunction(key)
        current = self.myHashSet[index]
        while current.next:
            if current.next.key == key:
                return True
            current = current.next
        return False

```

### solution - java
```java

class ListNode{
    int key;
    ListNode next;
    ListNode(int key){
        this.key = key;
        this.next = null;
    }
}

class MyHashSet {
    private ListNode hashset[];

    public MyHashSet() {
        hashset = new ListNode[10000];
    }

    private int hashFunction(int key){
        return key % 10000;
    }
    
    public void add(int key) {
        int index = hashFunction(key);
        ListNode current = hashset[index];
        if (current == null) {
            hashset[index] = new ListNode(key);
            return ;
        }
        if(current.key == key){
            return ;
        }
        while(current.next != null){
            if(current.key == key){
                return;
            }
            current = current.next;
        }
        current.next = new ListNode(key);

    }
    
    public void remove(int key) {
        int index = hashFunction(key);
        ListNode current = hashset[index];
        if(current == null){
            return;
        }
        if(current.key == key){
            hashset[index] = current.next;
            return;
        }

        while(current.next != null){
            if(current.next.key == key){
                current.next = current.next.next;
                return;
            }
            current = current.next;
        }
    }
    
    public boolean contains(int key) {
        int index = hashFunction(key);
        ListNode current = hashset[index];
        while(current != null){
            if(current.key == key){
                return true;
            }
            current = current.next;
        }
        return false;
    }
}

/*

class Test{

    public static void main(String[] args) {

        MyHashSet myHashSet = new MyHashSet();
        myHashSet.add(1);
        myHashSet.add(2);
        System.out.println(myHashSet.contains(1));  // Output: true
        System.out.println(myHashSet.contains(3));  // Output: false
        myHashSet.add(2);
        System.out.println(myHashSet.contains(2));  // Output: true
        myHashSet.remove(2);
        System.out.println(myHashSet.contains(2));  // Output: false
    
        
    }
}mod
*/

```

---

## 706. Design HashMap - Easy

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input

    ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

Output

    [null, null, null, 1, -1, null, 1, null, -1]

Explanation

    MyHashMap myHashMap = new MyHashMap();
    myHashMap.put(1, 1); // The map is now [[1,1]]
    myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
    myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
    myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
    myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
    myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
    myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
    myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

 

Constraints:

    0 <= key, value <= 106
    At most 104 calls will be made to put, get, and remove.



### solution - python
```py
'''

there will be collison
when hash function returns the same result for different keys
multiple values could be stored at the same location
- to solve it
    - open addressing
    - chanining

    
1 : 20
1001  : 30

index : value (key, value)
0   
1   : 0 -> (1, 20) -> (1001, 30)
2
.
.
.
9999

'''

class ListNode:
    def __init__(self, key = -1, value=-1):
        self.key = key
        self.value =value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.myhasmap = [ListNode(0,0) for i in range(10000)]

    def _hashFunction(self, key):
        return key % 10000

    def put(self, key: int, value: int) -> None:
        index = self._hashFunction(key)
        current = self.myhasmap[index]
        while current.next:
            if current.next.key == key:
                current.next.value = value
                return
            current= current.next
        current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hashFunction(key)
        current = self.myhasmap[index]
        while current.next:
            if current.next.key == key:
                return current.next.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = self._hashFunction(key)
        current = self.myhasmap[index]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def printOut(self, index):
        current = self.myhasmap[index]
        ans = str(current.next.key)+ " : "
        while current.next:
            ans  = ans + str(current.next.value) + " -> "
            current = current.next
        print(ans)
        

        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2 )
print(obj.get(1))
print(obj.get(3))
obj.put(2,1)

obj.printOut(2)

# obj.get(2)
# obj.remove(2)
# obj.get(2)

# print(obj.get(10001))
# obj.remove(10001)
# print(obj.get(10001))


```

---
## 21. Merge Two Sorted Lists - Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 

The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

Example 2:

        Input: list1 = [], list2 = []
        Output: []

Example 3:

        Input: list1 = [], list2 = [0]
        Output: [0]
 

Constraints:

        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.

### solution - python
```py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self, list1:ListNode, list2:ListNode) :
        # If the first linked list is empty
        if not list1:
            return list2
        # If the second linked list is empty
        elif not list2:
            return list1
        # Pick the smaller value between the two lists values
        else:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
   
   

```

### solution - java
```java

```

---

## 60. Intersection of Two Linked Lists - Easy

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.




The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

    The inputs to the judge are given as follows (your program is not given these inputs):

    - intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
    
    - listA - The first linked list.

    - listB - The second linked list.
    
    - skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    
    - skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:


Input: 

    intersectVal = 8, 
    listA = [4,1,8,4,5], 
    listB = [5,6,1,8,4,5], 
    skipA = 2, 
    skipB = 3

Output: 
    Intersected at '8'

Explanation: 

    The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).

    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
    
    There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

    - Note that the intersected node's value is not 1 because the nodes 
    with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. 
    
    In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

Example 2:


Input: 

    intersectVal = 2, 
    listA = [1,9,1,2,4], 
    listB = [3,2,4], 
    skipA = 3, 
    skipB = 1

Output: 
    Intersected at '2'

Explanation: 

    The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).

    From the head of A, it reads as [1,9,1,2,4].
    
    From the head of B, it reads as [3,2,4]. 
    
    There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: 

    intersectVal = 0, 
    listA = [2,6,4], 
    listB = [1,5], 
    skipA = 3, 
    skipB = 2

Output: 
    No intersection

Explanation: 

    From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. 
    
    Since the two lists do not intersect, intersectVal must be 0, 
    
    while skipA and skipB can be arbitrary values.

    Explanation: The two lists do not intersect, so return null.
 

Constraints:

    The number of nodes of listA is in the m.

    The number of nodes of listB is in the n.

    1 <= m, n <= 3 * 104
    1 <= Node.val <= 105
    0 <= skipA < m
    0 <= skipB < n

    intersectVal is 0 if listA and listB do not intersect.

    intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

 

Follow up:
    Could you write a solution that runs in O(m + n) time and use only O(1) memory?

### solution - python
```py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA_pointer = headA
        headB_pointer = headB
        hashSet = set()        
        while headA_pointer:
            hashSet.add(id(headA_pointer))
            headA_pointer = headA_pointer.next
        
        while headB_pointer:
            if id(headB_pointer) in hashSet:
                return headB_pointer
            headB_pointer = headB_pointer.next

        return None

```

### solution - java
```java

```