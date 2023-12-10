#Task 1

#Extend UnorderedList

#Implement append, index, pop, insert methods for UnorderedList. Also implement a slice method, which will take two parameters start and stop, and return a copy of the list starting at the position and going up to but not including the stop position.

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} not found in the list")

    def pop(self, pos=None):
        if pos is None:
            pos = self.size() - 1

        if pos < 0 or pos >= self.size():
            raise IndexError("pop index out of range")

        if pos == 0:
            popped_item = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            popped_item = current.next.data
            current.next = current.next.next

        return popped_item

    def insert(self, pos, item):
        if pos < 0 or pos > self.size():
            raise IndexError("insert index out of range")

        new_node = Node(item)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def slice(self, start, stop):
        if start < 0 or stop > self.size() or start > stop:
            raise ValueError("Invalid slice parameters")

        sliced_list = UnorderedList()
        current = self.head

        for i in range(stop):
            if i >= start:
                sliced_list.append(current.data)
            current = current.next

        return sliced_list

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)

    print("Original list:", [item for item in my_list])
    
    print("Index of 3:", my_list.index(3))

    popped_item = my_list.pop()
    print("Popped item:", popped_item)
    print("List after pop:", [item for item in my_list])

    my_list.insert(1, 5)
    print("List after insert at index 1:", [item for item in my_list])

    sliced_list = my_list.slice(1, 3)
    print("Sliced list:", [item for item in sliced_list])
