class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singly:
    def __init__(self):
        self.head = None

    def add_end(self, val):
        new_node = node(val)
        last = self.head
        if self.head == None:
            self.head = new_node
        else:
            while last.next:
                last = last.next
            last.next = new_node

    def print_ll(self):

        self.temp = self.head

        while self.temp is not None:
            print(self.temp.data)
            self.temp = self.temp.next


def main():
    val = 0
    ll = singly()

    while(True):
        val = int(input("Enter the value: "))
        if val == -1:
            break
        ll.add_end(val)

    ll.print_ll()

if __name__ == "__main__":
    main()