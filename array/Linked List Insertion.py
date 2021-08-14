class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


#At the front of the linked list

    def insertFront(self, val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node

# Add the node after a given node

    def insertAfter(self,pre_node,val):
        new_node=Node(val)
        new_node.next=pre_node.next
        pre_node.next=new_node

#Add a node at the end

    def insertAtEnd(self,val):
        new_node=Node(val)

        if self.head is None:
            self.head=new_node
            return

        last=self.head
        while (last.next):
            last=last.next


        last.next=new_node

#print Linked List

    def printList(self):
        last=self.head
        while(last):
            print (last.data,end='')
            last=last.next
            

# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
    print(llist.printList())
 
    # Insert 6.  So linked list becomes 6->None
    llist.insertFront(6)
    print(llist.printList())
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.insertFront(7)
    print(llist.printList())
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.insertFront(1)
    print(llist.printList())
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.insertAtEnd(4)
    print(llist.printList())
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)
 
    print('Created linked list is:',)
    print(llist.printList())
                
    
    
    
