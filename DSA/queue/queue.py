# Creation d'une classe Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creation d'une classe Queue pour la Queue
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # Creation d'une methode d'ajout de donnee dans la queue
    def enqueue(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = self.tail = new_node
            print(f"{self.head.data} has been added")
        else:
            new_node.next = self.head
            self.head = new_node
            print(f"{self.head.data} has been added")

    # Creation d'une methode pour retirer un element de la queue
    def dequeue(self):
        if self.head is None:
            print("Il n'y a rien a retire la queue est vide")
            return None
        else:
            dequeued_node = self.head
            self.head = self.head.next
            self.tail.next = None
            dequeued_node.next = None
            print(f"{dequeued_node.data} a ete retire de la queue")
            return dequeued_node.data
        
    # Creation d'une methode peeking into the queue
    def peeking(self):
        if self.head:
            print(f"The first element is {self.head.data}")
            return self.head.data
        else:
            print("Il n'y a rien a retire la queue est vide")
            return None
        
my_queue = Queue()
my_queue.enqueue("Abbas")
my_queue.enqueue("Moctar")
my_queue.dequeue()
my_queue.enqueue("Isamel")
my_queue.enqueue("Moctar")
my_queue.peeking()