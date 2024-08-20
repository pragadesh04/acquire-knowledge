class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = node(data)

        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def print_(self, msg):
        print(msg,"\n")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    def sort(self):
        temp = self.head
        cur = temp.next
        val = temp.data

        while temp is not None:
            cur = temp.next
            while cur is not None:
                if temp.data > cur.data:
                    val = cur.data
                    cur.data = temp.data
                    temp.data = val
                cur = cur.next
            temp = temp.next

singly = sll()

val = 0

while True:
    val = int(input())
    if val == -1:
        break
    singly.add(val)

singly.print_("Before Swapping")
singly.sort()
singly.print_("After Swapping")