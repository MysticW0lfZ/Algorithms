from DoubleLinkNode import DoubleLinkNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeAtRear(self, item):
        myNode = DoubleLinkNode(item)
        if self.head is None and self.tail is None:
            # Empty list, set head and tail to the new node
            self.head = myNode
            self.tail = myNode
        else:
            # Link the current tail node to the new node
            self.tail.setNext(myNode)
            myNode.setPrevious(self.tail)
            # Update the tail to the new node
            self.tail = myNode

    def insertNodeAtFront(self, item):
        myNode = DoubleLinkNode(item)
        if self.head is None and self.tail is None:
            # Empty list, set head and tail to the new node
            self.head = myNode
            self.tail = myNode
        else:
            # Link the new node to the current head node
            self.head.setPrevious(myNode)
            myNode.setNext(self.head)
            # Update the head to the new node
            self.head = myNode

    def traverseLinkedList(self):
        length = 140
        print("+" * length)
        print("Exploring the Doubly Linked List: ")
        print("+" * length)
        temp = self.head
        while temp is not None:
            print(temp, end='')
            temp = temp.getNext()
        print('\n' + "+" * length)
