

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

'''
a = ListNode(1)
b = ListNode(0)
c = ListNode(1)
# d = ListNode(1)
# e = ListNode(0)
# f = ListNode(1)'''




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
    '''
    or return reverseList_recurssive(head=temp, prevoius=head)
    and remove the variables
    ''' 

    return reverseList_recurssive(head=temp, previous=head)



printOut(a)
printOut(reverseList_recurssive(a))




# ====================================