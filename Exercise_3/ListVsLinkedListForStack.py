"""
    Comparison of running time between List and Linked List for implementing a Stack.

    @ Author: Dr. Romas James Hada
"""

import time
import random

from StackArrayTypeTwo import StackArrayTypeTwo
from Stack import Stack
from StackArray import StackArray


def printMessage(symbol, length, msg):
    print(symbol * length)
    print(msg)
    print(symbol * length)


def computeRunningTimeForStacks(myStack, numElements):
    print(myStack)
    start = time.time()
    for i in range(numElements):
        myStack.push(random.randint(0, 1000))

    for i in range(int(0.99 * numElements)):
        myStack.pop()

    printMessage('+', 140, f"Top: {myStack.peek()}")

    for i in range(int(2 * numElements)):
        myStack.push(random.randint(0, 1000))

    end = time.time()

    printMessage('*', 140, f"Total Running Time: {end - start} sec.")


if __name__ == '__main__':
    userChoice = ''
    while True:
        try:
            printMessage('+', 140, 'Please Enter Number of Elements: ')
            numberOfElements = int(input('> '))

            if numberOfElements >= 100:
                myStackWithLinkedList = Stack()
                myStackWithList = StackArray()
                myStackWithListTypeTwo = StackArrayTypeTwo()

                printMessage('*', 140, "Running Time for Stack using a Linked List: ")
                computeRunningTimeForStacks(myStackWithLinkedList, numberOfElements)

                printMessage('*', 140, "Running Time for Stack using Array (List):")
                computeRunningTimeForStacks(myStackWithList, numberOfElements)

                printMessage('*', 140, "Running Time for Stack using Array (List) Type Two:")
                computeRunningTimeForStacks(myStackWithListTypeTwo, numberOfElements)
            else:
                printMessage('*', 140, "Number of Elements must be greater than or equal to 100.")
        except ValueError:
            printMessage('+', 140, "Please Enter a Valid Number!")

        userChoice = input('Do you want to continue (Y/N)? ')
        if userChoice.lower() == 'n':
            break


