"""
    A Node of a Tree

    @ Author: Dr. Romas James Hada
"""


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def setLeftChild(self, newNode):
        self.left = newNode
        newNode.setParent(self)

    def setRightChild(self, newNode):
        self.right = newNode
        newNode.setParent(self)

    def setParent(self, parentNode):
        self.parent = parentNode

    def setData(self, newNode):
        self.data = newNode

    def getData(self):
        return self.data

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getParent(self):
        return self.parent

    def isLeafNode(self):
        pass    # Complete this part ...

    def __str__(self):
        if self.data is None:
            return "Empty!"
        else:
            return f"[{self.data}]"


