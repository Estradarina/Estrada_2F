# Assessment 3.2: Linear Data Structure - STACK
# A stack follows LIFO (Last In, First Out).

stack = list("ESTRADA")

def display():
    if stack:
        print("Stack (bottom -> top):", stack)
        print("Top element:", stack[-1])
    else:
        print("Stack is empty.")

while True:
    print("\n===== STACK MENU =====")
    print("1. Display stack")
    print("2. PUSH a letter")
    print("3. POP the top letter")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        display()

    elif choice == "2":
        letter = input("Enter one letter to PUSH: ").strip().upper()
        if len(letter) == 1 and letter.isalpha():
            stack.append(letter)
            print(letter, "was PUSHED onto the stack.")
            display()
        else:
            print("Please enter exactly one alphabetic letter.")

    elif choice == "3":
        if stack:
            removed = stack.pop()
            print("POPPED from the stack:", removed)
            display()
        else:
            print("Stack is empty. Nothing to POP.")

    elif choice == "4":
        print("Program ended. Thank you!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
