class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class singly:
    def __init__(self):
        self.head = None
    def add(self, data):
        self.data = data
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def print_(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")
        
    def minmax(self):
        min, max, temp = self.head.data, self.head.data, self.head
        if self.head is None:
            print("No element")
            return
        while temp.next:
            if temp.data < min:
                min = temp.data
            if temp.data > max:
                max = temp.data
            temp = temp.next
        return {"min":min, "max":max}

sll = singly()
while True:
    val = int(input("Enter the value: "))
    if val == -1:
        break
    sll.add(val)
sll.print_()

print("Minimum of the list is: ")
print(sll.minmax()["min"])
print("Maximum of the list is: ")
print(sll.minmax()["max"])