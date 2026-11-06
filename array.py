# Assessment 3.2: Linear Data Structure - ARRAY
# The program starts with the letters of the surname ESTRADA.
# An array is represented by a Python list.

letters = ["E", "S", "T", "R", "A", "D", "A"]

def display():
    print("\nCurrent array:", letters if letters else "[]")

while True:
    print("\n===== ARRAY MENU =====")
    print("1. Display array")
    print("2. Add a letter")
    print("3. Remove the first letter")
    print("4. Remove a letter by position")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        display()

    elif choice == "2":
        letter = input("Enter one letter to add: ").strip().upper()
        if len(letter) == 1 and letter.isalpha():
            letters.append(letter)
            print(letter, "was added to the array.")
            display()
        else:
            print("Please enter exactly one alphabetic letter.")

    elif choice == "3":
        if letters:
            removed = letters.pop(0)
            print("Removed first letter:", removed)
            display()
        else:
            print("Array is empty. Nothing to remove.")

    elif choice == "4":
        if letters:
            display()
            try:
                position = int(input("Enter position to remove (1 to " + str(len(letters)) + "): "))
                if 1 <= position <= len(letters):
                    removed = letters.pop(position - 1)
                    print("Removed:", removed)
                    display()
                else:
                    print("Position is out of range.")
            except ValueError:
                print("Please enter a valid whole number.")
        else:
            print("Array is empty. Nothing to remove.")

    elif choice == "5":
        print("Program ended. Thank you!")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
