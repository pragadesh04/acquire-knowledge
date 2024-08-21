class node:
    def __init__ (self, data):
        self.data =data
        self.next = None
        self.prev = None
    
class double:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def print_(self, msg = ""):
        print(f"\n{msg}")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
