'''
stack = []
MAX = 5

for i in range(MAX):
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(stack) == MAX:
            print("Stack Overflow!")
        else:
            value = int(input("Enter value: "))
            stack.append(value)
            print("Element pushed successfully.")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow!")
        else:
            print("Popped element:", stack.pop())

    elif choice == 3:
        print("Stack elements:", stack[::-1])

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")'''



queue = []
MAX = 5

for i in range(MAX):
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == MAX:
            print("Queue Overflow!")
        else:
            value = int(input("Enter value: "))
            queue.append(value)
            print("Element inserted successfully.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow!")
        else:
            print("Deleted element:", queue.pop(0))

    elif choice == 3:
        print("Queue elements:", queue)

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
