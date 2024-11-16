"""
    Implementing Queue using list (array).
    Queue with Insertion from the rear side and Removal from the front side.

    @ Author: Dr. Romas James Hada
"""


class QueueUsingList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def traverse(self):
        print("*" * 140)
        index = 0
        for item in self.queue:
            if index == len(self.queue) - 1:
                print(item)
            else:
                print(item, end=' ')
            index += 1
        print("*" * 140)

    def __str__(self):
        return f"This is a Queue Implemented Using List (Array)!"

