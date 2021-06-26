# This file is the version I created without referencing the documentation.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class List:
    def __init__(self):
        self.head = None

    def __str__(self):
        iterator = self.head
        item = 1
        repr_string = ''
        while iterator is not None and item < 100:
            repr_string.join(f'Value #{item}: {iterator.value}\n')
            item += 1
            iterator = iterator.next
        return repr_string


    def add_to_front(self, val):
        new_node = Node(val)
        old_head = self.head
        new_node.next = old_head
        self.head = new_node
        return self

    def add_to_back(self, val):
        new_node = Node(val)
        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next
        iterator.next = new_node
        return self

    def print_values(self):
        iterator = self.head
        item = 1
        while iterator != None and item < 100:
            print(f'Value #{item}: {iterator.value}')
            item += 1
            iterator = iterator.next
        print()
        return self

    def remove_from_front(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def remove_from_back(self):
        if self.head is None:
            return None
        iterator = self.head
        while iterator.next != None:
            iterator = iterator.next
        value = iterator.next.value
        iterator.next = None

        return value

    def remove_val(self, val):
        previous_iterator = None
        iterator = self.head
        while iterator is not None:
            print(f'{val}\t{iterator.value}\t{iterator.next}')
            if iterator.value == val:
                if iterator == self.head:
                    print(f'Value {val} found at head')
                    self.head = iterator.next
                    return self
                elif iterator.next == None:
                    print(f'Value {val} found at tail')
                    previous_iterator.next = None
                    return self
                else:
                    print(f'Value {val} found mid-list')
                    previous_iterator.next = iterator.next
                    return self
            else:
                previous_iterator = iterator
                iterator = iterator.next
        return self

    def insert_at(self, val, pos):
        previous_iterator = None
        iterator = self.head
        currpos = 0
        while (currpos < pos) and (iterator is not None):
            previous_iterator = iterator
            iterator = iterator.next
            currpos += 1

        # If we reached the end of the list but didn't get to the right position
        if (iterator is None) and (currpos != pos):
            print(f'Error: Cannot insert at position {pos}, as this is past the end of the list.')
            return self

        new_node = Node(val)
        new_node.next = iterator
        if pos == 0:
            self.head = new_node
        else:
            previous_iterator.next = new_node
        return self
