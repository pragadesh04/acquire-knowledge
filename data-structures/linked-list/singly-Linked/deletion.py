class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head=None
    def add(self, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def print__(self, msg):
        print()
        print(msg)
        temp = self.head
        if temp is None:
            print("Empty")
            return
        while temp:
            print(temp.data, end="->")
            temp = temp.next
    
    def delete_begin(self):
        self.head = self.head.next
    def delete_end(self):
        temp = self.head
        if temp.next is None:
            print("No element")
            return
        if temp is None:
            print("no element")
            return
        while temp.next.next:
            temp = temp.next
        temp.next = None
    def delete_pos(self, pos):
        temp = self.head
        if temp == None:
            return
        if pos == 0:
            self.delete_begin()
        for _ in range (pos-1):
            if temp.next is None:
                return
            temp = temp.next
        if temp.next is None:
            return
        temp.next = temp.next.next

singly = sll()
val = 0
while True:
    val = int(input())
    if val == -1:
        break
    singly.add(val)

singly.print__("before deletion")
singly.delete_begin()
singly.print__("After deletion")
singly.delete_end()
singly.print__("After deletion")
print("\n")
pos = int(input("enter The position\n"))
singly.delete_pos(pos)
singly.print__("After deletion")