# Assessment 3.2: Linear Data Structure - LINKED LIST
# Each node stores a letter and a reference to the next node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_first(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def display(self):
        if self.head is None:
            print("Linked list: NULL (empty)")
            return

        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        print("Linked list:", " -> ".join(values), "-> NULL")

linked_list = LinkedList()

# Initial data from Assessment 3.1: ESTRADA
for letter in "ESTRADA":
    linked_list.insert_end(letter)

while True:
    print("\n===== LINKED LIST MENU =====")
    print("1. Display linked list")
    print("2. Insert a letter at the end")
    print("3. Delete the first node")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        linked_list.display()

    elif choice == "2":
        letter = input("Enter one letter to insert: ").strip().upper()
        if len(letter) == 1 and letter.isalpha():
            linked_list.insert_end(letter)
            print(letter, "was inserted.")
            linked_list.display()
        else:
            print("Please enter exactly one alphabetic letter.")

    elif choice == "3":
        removed = linked_list.delete_first()
        if removed is None:
            print("Linked list is empty. Nothing to delete.")
        else:
            print("Deleted first node:", removed)
            linked_list.display()

    elif choice == "4":
        print("Program ended. Thank you!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
