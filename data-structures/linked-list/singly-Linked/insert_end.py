class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None
    
    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def print_ll(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data, end = " -> ")
            self.temp = self.temp.next
        print("None")

ll = sll()
while True:
    val = int(input())
    if val == -1:
        break
    ll.add_end(val)
ll.print_ll()