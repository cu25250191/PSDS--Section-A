#Stack Using Linked LIst 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    def pop(self):
        if self.top is None:
            print("Stack Underflow!")
        else:
            print("Popped element:", self.top.data)
            self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()

#Queue Using Linked List 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into queue")

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow!")
        else:
            print("Deleted element:", self.front.data)
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Queue elements:", end=" ")

            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()
q.display()
