class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")


var = SinglyLinkList()
var.insert_node(10)
var.insert_node(20)
var.insert_node(30)
var.insert_node(40)
var.display()