

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

public class Test {

    public static void printOut(ListNode head){
        ListNode current = head;
        while(current != null){
            System.out.print(current.val + " -> ");
            current = current.next;
        }
        System.out.println(" null ");
    }

    public static int getDecimalValue_old(ListNode head){
        ListNode current = head;
        int ans = 0;
        while(current != null){
            ans = (ans * 2 )+ current.val;
            current = current.next;
        }
        return ans;

    }
    public static int getDecimalValue(ListNode head){
        ListNode current = head;
        String strAns = "";
        while(current != null){
            strAns = strAns + Integer.toString(current.val);
            current = current.next;
        }
        return Integer.parseInt(strAns, 2);

    }

    public static int getNodeLength(ListNode head) {
        ListNode current = head;
        int ans = 0;
        while (current != null ) {
            ans += 1;
            current = current.next;
        }
        return ans;
    }

    public static int middleNode_old(ListNode head) {
        int nodelegth = getNodeLength(head);
        int midVal = nodelegth / 2;
        ListNode current = head;
        int index = 0;
        while(current != null && index < midVal){
            current = current.next;
            index += 1;
        }
        return current.val;

    }

    // clever
    public static int middleNode(ListNode head) {

        ListNode temp = head;
        
        while(temp != null && temp.next != null){
            head = head.next;
            temp = temp.next.next;            
        }
        return head.val;


    }

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
    
    public static ListNode reverseList_recurssive(ListNode head, ListNode previous) {
        if(head == null){
            return previous;
        }
        ListNode next = head.next;
        head.next = previous;
        return reverseList_recurssive(next, head);
    }

    public static void main(String[] args) {

        ListNode a = new ListNode(1);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(3);
        ListNode d = new ListNode(4);
        ListNode e = new ListNode(5);
        ListNode f = new ListNode(6);

        a.next = b;
        b.next = c;
        c.next = d;
        d.next = e;
        e.next = f;

        // printOut(a);

        // System.out.println(getDecimalValue(a));

        // node length
        // System.out.println(getNodeLength(a));

        // middle node
        // System.out.println(middleNode(a));


        // reverse List
        printOut(a);
        // printOut(reverseList(a));
        printOut(reverseList_recurssive(a, null));
        

         
  

    }
}





