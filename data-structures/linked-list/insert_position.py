class node:
    def __init__(self, data):
        self.next = None
        self.data= data
        
class ll:
    def __init__(self):
        self.head = None 
    def add_pos(self, pos, data):
        new_node = node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp = self.head
            for _ in range (pos-1):
                if temp is None or temp.next is None:
                    print("Give proper position")
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            
    def print_ll(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data, end = " - ")
            self.temp = self.temp.next
        print("None")
            
ll = ll()
ll.add_pos(0, 5)
ll.add_pos(1, 4)
ll.add_pos(2, 5)
ll.add_pos(3, 7)
ll.add_pos(4, 2)

while True:
    val =int(input())
    if val ==-1:
        break
    pos = int(input())
    ll.add_pos(pos, val)
    ll.print_ll()