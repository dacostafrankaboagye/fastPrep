
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


        
    


#============================================
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
  

'''


'''

hash map

0   = 0 -> 20000 -> 30000 ->
1
2
.
.
9999

'''

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


    


#==========================================================================

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
'''


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
        

        

        






