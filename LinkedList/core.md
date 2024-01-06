## Linked List - Python

```py

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next


a = ListNode(1)
b = ListNode(0)
c = ListNode(1)
# d = ListNode(1)
# e = ListNode(0)
# f = ListNode(1)

a.next = b
b.next = c
# c.next = d
# d.next = e
# e.next = f

#print - out
def printOut(head):
    current = head
    while current is not None:
        print(current.val, end= ' -> ')
        current = current.next
    print("None")


def nodeLength(head):
    ans = 0
    while head:
        head = head.next
        ans +=1
    return ans


def middleNode(head):
    temp = head
    while temp and temp.next:
        head = head.next
        temp = temp.next.next
    return head.val



def reverseList(head):
    current = head
    previous = None
    while current:
        temp = current.next
        current.next = previous
        previous = current
        current = temp 
    return previous

def reverseList_recurssive(head, previous=None):
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

    return reverseList_recurssive(head=temp, previous=head)

```

## Linked List - Java

```java


class ListNode {
    int val;
    ListNode next;

    ListNode(){}

    ListNode(int val){
        this.val = val;
    }

    ListNode(int val, ListNode next){
        this.val = val;
        this.next= next;
    }
}


//print-out
public static void printOut(ListNode head){
    ListNode current = head;
    while(current != null){
        System.out.print(current.val + " -> ");
        current = current.next;
    }
    System.out.println(" null ");
}


// node length
public static int getNodeLength(ListNode head) {
    ListNode current = head;
    int ans = 0;
    while (current != null ) {
        ans += 1;
        current = current.next;
    }
    return ans;
}


// middle node element
    // clever
public static int middleNode(ListNode head) {

    ListNode temp = head;

    while(temp != null && temp.next != null){
        head = head.next;
        temp = temp.next.next;
    }
    return head.val;


}



// reverse - iterative
public static ListNode reverseList(ListNode head) {
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

// reverse - recurssive
public static ListNode reverseList_recurssive(ListNode head, ListNode previous) {
    if(head == null){
        return previous;
    }
    ListNode next = head.next;
    head.next = previous;
    return reverseList_recurssive(next, head);
}

```
