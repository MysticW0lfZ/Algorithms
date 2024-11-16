from Assignment_1.DoublyLinkedList import DoublyLinkedList


if __name__ == '__main__':
    myList = DoublyLinkedList()

    # Personalize the list with your To-Do items
    myList.insertNodeAtRear('Exercise / Yoga')
    myList.insertNodeAtRear('Meditate')
    myList.insertNodeAtRear('Read a Book')
    myList.insertNodeAtRear('Check Emails')
    myList.insertNodeAtRear('Check News')
    myList.insertNodeAtRear('Take a Shower')

    # Traverse and print the list
    myList.traverseLinkedList()

    # Insert at the front
    myList.insertNodeAtFront('Check Mobile Apps')

    # Traverse and print the list again
    myList.traverseLinkedList()

    # Display head and tail data
    print(f"Head: {myList.head.getData()}")
    print(f"Tail: {myList.tail.getData()}")
