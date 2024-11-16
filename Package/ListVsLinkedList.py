"""
    Comparison of running time between List and Linked List for implementing a Queue.

    @ Author: Dr. Romas James Hada
"""
import time
import random

from Queue import Queue
from QueueUsingList import QueueUsingList


def printMessage(symbol, length, msg):
    print(symbol * length)
    print(msg)
    print(symbol * length)


def computeRunningTimeForQueues(myQueue, numElements):
    print(myQueue)
    start = time.time()
    for i in range(numElements):
        myQueue.enqueue(random.randint(0, 1000))

    for i in range(int(0.999 * numElements)):
        myQueue.dequeue()

    myQueue.traverse()

    for i in range(int(0.1 * numElements)):
        myQueue.enqueue(random.randint(0, 1000))

    end = time.time()
    printMessage('*', 140, f"Total Running Time: {end - start} sec.")


if __name__ == '__main__':
    userChoice = ''
    while True:
        try:
            printMessage('+', 140, 'Please Enter Number of Elements: ')
            numberOfElements = int(input('> '))

            if numberOfElements >= 100:
                myQueueWithLinkedList = Queue()
                myQueueWithList = QueueUsingList()

                printMessage('*', 140, "Running Time for Queue using a Linked List: ")
                computeRunningTimeForQueues(myQueueWithLinkedList, numberOfElements)

                printMessage('*', 140, "Running Time for Queue using Array (List):")
                computeRunningTimeForQueues(myQueueWithList, numberOfElements)
            else:
                printMessage('*', 140, "Number of Elements must be greater than or equal to 100.")
        except ValueError:
            printMessage('+', 140, "Please Enter a Valid Number!")

        userChoice = input('Do you want to continue (Y/N)? ')
        if userChoice.lower() == 'n':
            break
