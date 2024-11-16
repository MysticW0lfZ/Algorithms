#James Mendez
#Assignment 2


def display_menu()
    print("Choose an option:")
    print("1) Insert an element to the list")
    print("2) Remove an element from the rear")
    print("3) Traverse the list")
    print("4) Quit")


def main():
    lst = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            element = input("Enter the element to insert at the front: ")
            lst.insert(0, element)  # Insert element at the front of the list
            print(f"Element '{element}' inserted at the front.")

        elif choice == 2:
            if lst:
                removed_element = lst.pop()  # Remove element from the rear
                print(f"Element '{removed_element}' removed from the rear.")
            else:
                print("List is empty. Nothing to remove.")

        elif choice == 3:
            if lst:
                print("Traversing the list:")
                for i, elem in enumerate(lst):
                    print(f"{i + 1}: {elem}")
            else:
                print("List is empty.")

        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
