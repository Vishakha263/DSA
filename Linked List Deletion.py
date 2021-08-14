class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    # Deleting a node

    def deleteNode(self, key):

        #case1: deleting the head
        
        if self.head!=None:
            if self.head.data==key:
                self.head=self.head.next
                return 
            
        # case2: deleting in middle
            else:
                n=self.head
                while(n.next==None or n.next.data!=key ):
                    if n.next == None:
                        return (print('Given key does not present'))
                    n=n.next
                
                n.next=n.next.next

    # print function

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end='')
            temp=temp.next


#driver code

llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
 
print ("Created Linked List: ")
llist.printList()
llist.deleteNode(5)
print ("\nLinked List after Deletion of 1:")
llist.printList()



            
        
