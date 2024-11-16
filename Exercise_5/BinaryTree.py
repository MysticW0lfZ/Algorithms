"""
    A Binary Tree

    @ Author: Dr. Romas James Hada
"""
from TreeNode import TreeNode


def printMessage(symbol, length, msg):
    print(symbol * length)
    print(msg)
    print(symbol * length)


def traverseAndPrintRoot(myNode):
    print(f"Root of the tree is: {myNode.getData()}")


def preOrderTraversal(root):
    if root:
        print(root.getData())
        preOrderTraversal(root.getLeftChild())
        preOrderTraversal(root.getRightChild())

def inOrderTraversal(root):
   if root:
       inOrderTraversal(root.getLeftChild())
       print(root.getData())
       inOrderTraversal(root.getRightChild())


def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.getLeftChild())
        postOrderTraversal(root.getRightChild())
        print(root.getData())

if __name__ == '__main__':
    food = TreeNode('Food')
    #fruits
    fruits = TreeNode('Fruits')
    apple = TreeNode('Apples')
    berries = TreeNode('Berries')
    blueberries = TreeNode('Blueberries')
    blackberries = TreeNode ('Blackberries')
    food.setLeftChild(fruits)

    fruits.setLeftChild(apple)

    print(food.getLeftChild().getLeftChild())

    food.setRightChild(berries)
    food.setLeftChild(blueberries)
    food.setRightChild(blackberries)
    #vegetables
    vegetables = TreeNode('Vegetables')
    broccoli = TreeNode ('broccoli')
    cabbage = TreeNode ('Cabbage')
    napacabbage = TreeNode('Napa Cabbage')
    redcabbage = TreeNode('Red Cabbage')
    food.setRightChild(vegetables)
    
    # Complete this part ...

    printMessage('*', 44, "Pre-Order Traversal ...")
    preOrderTraversal(food)

    printMessage('+', 44, "In-Order Traversal ...")
    inOrderTraversal(food)

    printMessage('+', 44, "Post-Order Traversal ...")
    postOrderTraversal(food)
    
    printMessage('*', 44, "End of Program ...")
    
    # Bonus Problem Starts Here ...


