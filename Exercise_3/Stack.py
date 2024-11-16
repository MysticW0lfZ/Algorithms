from DoublyLinkedList import DoublyLinkedList

"""
    Stack with push and pop from the rear side.
    
    @ Author: Dr. Romas James Hada
"""


class Stack(DoublyLinkedList):
    def push(self, obj):
        self.insertNodeAtRear(obj)

    def pop(self):
        self.removeLastNode()

    def peek(self):
        return self.tail

    def traverse(self):
        self.traverseLinkedList()

    def __str__(self):
        if self.head is not None:
            return self.head
        else:
            return 'This is an Empty Stack!'
