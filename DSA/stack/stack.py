# Creation d'un Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creation de la Stack
class Stack:
    def __init__(self):
        self.top = None

    # Cretion d'une methode d'ajout d'elements
    def add_item(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        print(f"{self.top.data} a ete ajoutee")
    
    # Creation d'une methode pour retirer un element
    def remove_item(self):
        if self.top is None:
            print("La stack ne contient aucune donnee")
            return None
        else:
            removed_node = self.top
            self.top = self.top.next
            removed_node.next = None
            print(f"{removed_node.data} a ete retire de la stack et le nouveau top est: {self.top.data}")
            return removed_node.data
        
    # Creation d'une mehtode peek pour voir le top element de la stack
    def peeking_in_stack(self):
        if self.top:
            print(f"Le top de la stack est {self.top.data}")
            return self.top.data
        else: 
            print("La stack ne contient aucune donnee")
            return None
        

my_stack = Stack()
my_stack.add_item("Abbas")
my_stack.add_item("Ismael")
my_stack.add_item("Ali")
my_stack.remove_item()
my_stack.peeking_in_stack()
