from Node import Node


class ASimpleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    linked_list = ASimpleLinkedList()

    while True:
        user_input = input("Enter a string to add to the linked list (or -1 to stop): ")
        if user_input == '-1':
            break
        linked_list.append(user_input)

    print("The linked list is:")
    linked_list.display()