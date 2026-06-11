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
            self.head = new_node
            self.tail = new_node
            print(f"{self.head.data} has been added")
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Creation d'une methode pour retirer un element de la queue
    def dequeue(self):
        if self.head is None:
            print("Il n'y a rien a retire la queue est vide")
            return None
        else:
            dequeued_node = self.head
            self.head = dequeued_node.next
            dequeued_node.next = None
            if self.head == None:
                self.tail = None
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