# Creating a node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a Linked list class that represent the actual linked list
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_data(self, data):
        data = Node(data)
        if not self.head:
            self.head = data
            self.tail = data
            return data
        else:
            self.head.tail = None
            self.tail = self.head.next
            self.head = data
            return data




my_list = Linked_list()

my_list.add_data("Abbas")

print(type(my_list))
