"""

    @ Author: Dr. Romas James Hada

    Node for Doubly Linked List
"""

from Node import Node


class DoubleLinkNode(Node):
    def __init__(self, _data):
        super().__init__(_data)
        self.prev = None

    def getPreviousNode(self):
        return self.prev

    def setPrevious(self, myPreviousNode):
        self.prev = myPreviousNode

    def __str__(self):
        if self.next is None:
            return f"{self.data}"
        else:
            return f"{self.data} <-> "
