"""

   @ Author: Dr. Romas James Hada

   Doubly Linked List
"""

from DoubleLinkNode import DoubleLinkNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeAtRear(self, item):
        myNode = DoubleLinkNode(item)
        if self.head is None and self.tail is None:
            self.head = myNode
            self.tail = myNode
        else:
            self.tail.setNext(myNode)
            myNode.setPrevious(self.tail)
            self.tail = myNode

    def insertNodeAtFront(self, item):
        myNode = DoubleLinkNode(item)
        if self.head is None and self.tail is None:
            self.head = myNode
            self.tail = myNode
        else:
            self.head.setPrevious(myNode)
            myNode.setNext(self.head)
            self.head = myNode

    def removeFirstNode(self):
        if self.head is None and self.tail is None:
            print("Removal Operation Failed! The Linked List is Empty!")
        elif self.head == self.tail:  # one node
            self.head = None
            self.tail = None
        else:
            temp = self.head    # firstNode
            self.head = temp.getNext() # new Node becomes the first node
            self.head.setPrevious(None)

            temp.setNext(None)  # detach the old node from the list

    def removeLastNode(self):
        if self.head is None and self.tail is None:
            print("Removal Operation Failed! The Linked List is Empty!")
        elif self.head == self.tail:  # one node
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = temp.getPreviousNode()  # change the pointer towards the second last node
            self.tail.setNext(None)

            temp.setPrevious(None)  # detach the old last node

    def traverseLinkedList(self):
        length = 140
        print("+" * length)
        print("Exploring the Doubly Linked List: ")
        print("+" * length)
        temp = self.head
        while True:
            if temp is None:
                break
            else:
                print(temp, end='')
                temp = temp.getNext()
        print('\n' + "+" * length)



