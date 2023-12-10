#Task 3

#Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. Any other element must remain on the stack respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message
#Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue. Any other element must remain in the queue respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, element):
        try:
            index = self.items.index(element)
            return self.items[index]
        except ValueError:
            raise ValueError(f"Element '{element}' not found in the stack")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def get_from_queue(self, element):
        try:
            index = self.items.index(element)
            return self.items[index]
        except ValueError:
            raise ValueError(f"Element '{element}' not found in the queue")


if __name__ == "__main__":
   
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    try:
        result = stack.get_from_stack(2)
        print(f"Element found in stack: {result}")
    except ValueError as e:
        print(e)

    try:
        result = stack.get_from_stack(4)
        print(f"Element found in stack: {result}")
    except ValueError as e:
        print(e)

    
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')

    try:
        result = queue.get_from_queue('b')
        print(f"Element found in queue: {result}")
    except ValueError as e:
        print(e)

    try:
        result = queue.get_from_queue('d')
        print(f"Element found in queue: {result}")
    except ValueError as e:
        print(e)



