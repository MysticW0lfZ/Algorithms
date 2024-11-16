"""
    A Binary Search Tree (BST)

    @ Author: Dr. Romas James Hada

"""
import random
from random import shuffle

from TreeNode import TreeNode


def printMessage(symbol, length, msg):
    print(symbol * length)
    print(msg)
    print(symbol * length)


def traverseAndPrintNode(myNode):
    if myNode.isLeafNode():
        print(myNode, end=' (Leaf Node)\n')
    else:
        print(myNode, end='\n')


def preOrderTraversal(parent):
    if parent is not None:
        traverseAndPrintNode(parent)
        preOrderTraversal(parent.getLeftChild())
        preOrderTraversal(parent.getRightChild())


def inOrderTraversal(parent):
    if parent is not None:
        inOrderTraversal(parent.getLeftChild())
        traverseAndPrintNode(parent)
        inOrderTraversal(parent.getRightChild())


def postOrderTraversal(parent):
    if parent is not None:
        postOrderTraversal(parent.getLeftChild())
        postOrderTraversal(parent.getRightChild())
        traverseAndPrintNode(parent)


def findNode(parentNode, _data):
    if parentNode is None:
        print(f"Node {_data} not found in the BST.")
        return None
    if _data == parentNode.getData():
        print(f"Node {_data} found in the BST.")
        return parentNode
    elif _data < parentNode.getData():
        return findNode(parentNode.getLeftChild(),_data)
    else:
        return findNode(parentNode.getRightChild(), _data)


def findParentNodeAndInsertNewNode(parentNode, _data):
    if _data <= parentNode.getData():
        if parentNode.getLeftChild() is not None:
            findParentNodeAndInsertNewNode(parentNode.getLeftChild(), _data)
        else:
            parentNode.setLeftChild(TreeNode(_data))
    else:
        if parentNode.getRightChild() is not None:
            findParentNodeAndInsertNewNode(parentNode.getRightChild(),_data)
        else:
            parentNode.setRightChild(TreeNode(_data))


def createABinarySearchTree(rootNode, myList):
    for data in myList:
        if rootNode.getData() is None:
            rootNode.setData(data)
        else:
            findParentNodeAndInsertNewNode(rootNode, data)


if __name__ == '__main__':
    root = TreeNode()
    listOfNumbers = [50, 23, 45, 16, 20, 1, 65, 55, 68]

    createABinarySearchTree(root, listOfNumbers)
    findNode(root, 69)
    printMessage('*', 44, "Insert Node 69 to the Existing BST ...")
    findParentNodeAndInsertNewNode(root, 69)
    findNode(root, 69)

    printMessage('*', 44, "Pre-Order Traversal ...")
    preOrderTraversal(root)

    printMessage('+', 44, "In-Order Traversal ...")
    inOrderTraversal(root)

    printMessage('+', 44, "Post-Order Traversal ...")
    postOrderTraversal(root)

    shuffle(listOfNumbers)
    printMessage('*', 55, "List After Shuffling ...")
    print(listOfNumbers)

    root = TreeNode()
    createABinarySearchTree(root, listOfNumbers)

    printMessage('*', 55, "Pre-Order Traversal After Shuffling the List ...")
    preOrderTraversal(root)

    printMessage('*', 55, "End of Program ...")
