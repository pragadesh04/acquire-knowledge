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
        i = 0
        while temp:
            print(temp.data, end=f"--")
            temp = temp.next
            i += 1
        print("None")

class input_:
    def inp(self):
        self.val = int(input("Enter the value: "))
        return self.val