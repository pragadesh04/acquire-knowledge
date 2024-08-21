class node:
    def __init__ (self, data):
        self.data =data
        self.next = None
        self.prev = None
    
class double:
    def __init__(self):
        self.head = None
        
    def add_start(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    def add_pos(self, data, pos):
        temp = self.head
        if pos == 0 or temp is None:
            self.add_start(data)
            return
        for _ in range(pos-1):
            if  temp.next is None:
                print("Reached end")
                return
            temp = temp.next
            
        new_node = node(data)
        new_node.next = temp.next
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def print_(self, msg):
        print(f"\n{msg}")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            
dll = double()
while True:
    val = int(input())
    if val == -1:
        break
    dll.add_start(val)
    
dll.print_("".center(50,"-"))
print()
a=int(input("0 to break or enter value to add at end?"))
if a:
    dll.add_end(a)
dll.print_("After  adding to end".center(50,"-"))

print()
b=input("0 to break or enter value and pos to add at end?").split(" ")
a = list(map(int,b))
print(a[0])
if a[0]:
    dll.add_pos(a[0], a[1])
dll.print_("After  adding to pos".center(50,"-"))