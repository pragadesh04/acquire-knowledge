class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class dcll:
    def __init__ (self):
        self.head = None
        self.last = None
        
    def add_begin(self, data):
        new_node = node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.last = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
            self.last.next = self.head
            self.head.prev = self.last
        
    def print_(self):
        temp = self.head
        while True:
            print(f"{temp.data}".center(25, " "))
            temp = temp.next
            if temp == self.head:
                break
    
class main:
    def ope(self):
        dc = dcll()
        while True:
            val = int(input("Enter the value: ".ljust(25, " ")))
            if val == -1:
                break
            dc.add_begin(val)
        dc.print_()
    
m = main()
m.ope()