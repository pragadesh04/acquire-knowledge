import utils as add
dll = add.double()

class sorting():
    def sort(self):
        temp = dll.head
        if temp is not None:
            while temp is not None:
                cur = temp.next
                while cur:
                    if temp.data > cur.data:
                        temp.data,cur.data = cur.data, temp.data
                    cur = cur.next
                temp=temp.next
            return
        else:
            print("Empty node")

s = sorting()
while True:
    val = int(input())
    if val == -1:
        break
    dll.add(val)
dll.print_()
s.sort()
dll.print_()