class CNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

var = CircularLinkList()
var.insert_node(10)
var.insert_node(20)
var.insert_node(30)
var.insert_node(40)
var.display()