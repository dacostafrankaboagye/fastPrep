
'''
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




a = ListNode(10)
b = ListNode(20)
c = ListNode(30)
d = ListNode(40)
e = ListNode(50)
f = ListNode(60)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

#print - out
def printOut(head):
    current = head
    while current is not None:
        print(current.val, end= ' -> ')
        current = current.next
    print("None")


def getDecimalValue(head):
    current = head
    strAns = '0b'
    while current is not None:
        strAns += str(current.val)
        current = current.next
    return int(strAns, base=0)


def nodeLength(head):
    ans = 0
    while head:
        head = head.next
        ans +=1
    return ans

def middleNode_old(head):
    nodelen = nodeLength(head)
    middleValue = nodelen // 2
    index = 0
    current = head
    while current and (index < middleValue):
        current = current.next
        index += 1
    return current.val

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
    
    # or return reverseList_recurssive(head=temp, prevoius=head)
    # and remove the variables
   

    return reverseList_recurssive(head=temp, previous=head)



printOut(a)
printOut(reverseList_recurssive(a))
'''



# ====================================
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
  



