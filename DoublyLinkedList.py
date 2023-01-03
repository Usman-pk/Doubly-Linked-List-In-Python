class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtHead(self, node):
        current = self.head
        node.previous = None
        self.head = node
        node.next = current

    def insertAtLast(self, node):
        current = self.head
        if current is not None:
            while current.next:
                current = current.next
            node.previous = current.next
            current.next = node
            node.next = None
        else:
            print("Double Linked List Is Empty")

    def printLinkedList(self):
        current = self.head
        print("\nDouble Linked List = ", end="")
        while current:
            if current is not None:
                print(current.value, "-> ", end="")
            current = current.next
        if current is None:
            print("NULL")


head = Node(3)
n2 = Node(4)
n3 = Node(7)
n4 = Node(10)
n5 = Node(11)
n6 = Node(15)


obj = DoublyLinkedList(head)
obj.insertAtLast(n2)
obj.insertAtLast(n3)
obj.insertAtLast(n4)
obj.insertAtLast(n5)
obj.insertAtLast(n6)


obj.printLinkedList()

n7 = Node(1)
obj.insertAtHead(n7)
obj.printLinkedList()

n8 = Node(11)
obj.deleteNode(n8)
obj.printLinkedList()