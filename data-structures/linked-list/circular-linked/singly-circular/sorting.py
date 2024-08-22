import sclutils as add
dll = add.scll()
class main():
    def sort(self):
        temp = dll.head
        while True:
            cur = temp.next
            while cur != dll.head:
                if temp.data > cur.data:
                    temp.data,cur.data = cur.data,temp.data
                cur = cur.next
            temp = temp.next
            if temp == dll.head:
                break
        else:
            print("Empty node")
s = main()
while True:
    val = int(input())
    if val == -1:
        break
    dll.add_begin(val)
dll.print_()
s.sort()
dll.print_("After Sorting")