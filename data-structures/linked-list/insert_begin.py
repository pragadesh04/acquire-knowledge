class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singly:
    def __init__(self):
        self.head = None
    
    def add_begin(self,val):
        new_node = node(val)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def print_ll(self):

        self.temp = self.head

        while self.temp is not None:
            print(self.temp.data)
            self.temp = self.temp.next

def inputing():

    val = 0
    ll = singly()

    while(True):
        val = int(input("Enter value: "))
        if val == -1:
            break
        ll.add_begin(val)

    ll.print_ll()
if __name__ == "__main__":
    inputing()