# Assessment 3.2: Linear Data Structure - QUEUE
# A queue follows FIFO (First In, First Out).

from collections import deque

queue = deque("ESTRADA")

def display():
    if queue:
        print("Queue (front -> rear):", list(queue))
        print("Front:", queue[0], "| Rear:", queue[-1])
    else:
        print("Queue is empty.")

while True:
    print("\n===== QUEUE MENU =====")
    print("1. Display queue")
    print("2. ENQUEUE a letter")
    print("3. DEQUEUE the front letter")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        display()

    elif choice == "2":
        letter = input("Enter one letter to ENQUEUE: ").strip().upper()
        if len(letter) == 1 and letter.isalpha():
            queue.append(letter)
            print(letter, "was ENQUEUED at the rear.")
            display()
        else:
            print("Please enter exactly one alphabetic letter.")

    elif choice == "3":
        if queue:
            removed = queue.popleft()
            print("DEQUEUED from the front:", removed)
            display()
        else:
            print("Queue is empty. Nothing to DEQUEUE.")

    elif choice == "4":
        print("Program ended. Thank you!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
