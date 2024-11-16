from DoublyLinkedList import DoublyLinkedList

"""
    Queue with Insertion from the rear side and Removal from the front side.
    
    @ Author: Dr. Romas James Hada
"""


class Queue(DoublyLinkedList):
    def enqueue(self, obj):
        self.insertNodeAtRear(obj)

    def dequeue(self):
        self.removeFirstNode()

    def traverse(self):
        self.traverseLinkedList()

    def __str__(self):
        if self.head is not None:
            return self.head
        else:
            return 'This is an empty Queue!'
