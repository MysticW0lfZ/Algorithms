"""
    Implementing Stack using array. Stack with push and pop from the front side.

    @ Author: Dr. Romas James Hada
"""


class StackArrayTypeTwo:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop(0)
        else:
            print("The Stack is Empty!")

    def peek(self):
        return self.stack[0]

    def traverse(self):
        print("*" * 140)
        index = 0
        for item in self.stack:
            if index == len(self.stack) - 1:
                print(item)
            else:
                print(item, end=' ')
            index += 1
        print("*" * 140)

    def __str__(self):
        return f"This is a Stack Implemented Using List (Array)! Push and Pop From the Front ..."

