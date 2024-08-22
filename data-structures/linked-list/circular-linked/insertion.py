class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class scll:
    def __init__(self):
        self.head = None
        self.last = None
    
    def add_begin(self, data):
        new_node = node(data)
        
        if self.head is None:
            self.head = new_node
            self.last = new_node
            new_node.next = self.head
            return
        
        new_node.next = self.head
        self.last.next = new_node
        self.head = new_node
    
    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.last = new_node
            return
        self.last.next = new_node
        new_node.next = self.head
        self.last = new_node
        
    def print_(self):
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

scll = scll()
val = 0
while True:
    val  = int(input("Enter the value to add: "))
    if val == -1:
        break
    scll.add_begin(val)
scll.print_()

val = int(input("Enter value to add at end: "))
scll.add_end(val)
scll.print_()