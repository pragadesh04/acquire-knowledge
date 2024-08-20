class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ll:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def print_ll(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data, end = " -> ")
            self.temp = self.temp.next
        print("None")

def main():
    linked = ll()
    data = 0
    while True:
        data = int(input())
        if data == -1:
            break
        linked.add_begin(data)
    linked.print_ll()

if __name__ == "__main__":
    main()