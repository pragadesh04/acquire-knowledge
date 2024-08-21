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

    def del_beg(self):
        temp = self.head
        self.head = temp.next
        self.head.prev = None

    def del_end(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next.prev = None
        temp.next = None

    def del_pos(self, pos):
        temp = self.head
        for _ in range (pos-1):
            if temp is None:
                print("out of Bound")
                return
            temp = temp.next
        
        if temp.next is not None:
            temp.next = temp.next.next
            temp.next.prev = temp

dll = double()
while True:
    val = int(input())
    if val == -1:
        break
    dll.add(val)
    
dll.print_()
dll.del_beg()
dll.print_()
dll.del_end()
dll.print_()
print()
pos = int(input("Enter Position to delete: "))
dll.del_pos(pos)
dll.print_()