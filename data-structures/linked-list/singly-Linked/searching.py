class node:
    def __init__(self,data):
        self.data=data
        self.next = None

class singly:
    def __init__(self):
        self.head = None
        
    def add(self,data):
        new_node = node(data)
        
        if self.head is None:
            print("created head")
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
    
    def searching(self, key):
        temp,i = self.head,0
        while temp:
            if temp.data == key:
                return i
            temp = temp.next
            i += 1
            
    def print_(self, msg):
        print(f"\n{msg}")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
            
sll = singly()
while True:
    val = int(input("enter the value: "))
    if val == -1:
        break
    sll.add(val)
    
sll.print_("The elements are")
key = int(input("Enter the Key to search: "))
print(sll.searching(key))