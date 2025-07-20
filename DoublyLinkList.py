class DNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkList():
    def __init__(self):
        self.head = None
    
    def insert_node(self,data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end="<->")
            current = current.next
        print("None")
    
var = DoublyLinkList()
var.insert_node(10)
var.insert_node(20)
var.insert_node(30)
var.insert_node(40)
var.insert_node(50)
var.display()