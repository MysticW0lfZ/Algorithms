"""

    @ Author: Dr. Romas James Hada

"""


class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def setNext(self, nextNode):
        self.next = nextNode

    def getNext(self):
        return self.next

    def setDisplayData(self, newData):
        self.data = newData

    def getData(self):
        return self.data

    def __str__(self):
        if self.next is None:
            return f"{self.data}"
        else:
            return f"{self.data} -> "
