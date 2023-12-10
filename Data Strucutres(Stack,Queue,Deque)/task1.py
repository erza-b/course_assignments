#Task 1

#Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

def reverse_sequence(input_sequence):
    stack = Stack()

    for char in input_sequence:
        stack.push(char)

    reversed_sequence = ""

   
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    return reversed_sequence

input_sequence = input("Enter a sequence of characters: ")


reversed_sequence = reverse_sequence(input_sequence)


print("Reversed sequence:", reversed_sequence)
