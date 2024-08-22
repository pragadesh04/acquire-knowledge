import sclutils as scl
sc = scl.scll()

class main:
    def delete_beg(self):
        sc.head = sc.head.next
        sc.last.next = sc.head
    def delete_end(self):
        temp = sc.head
        while True:
            temp= temp.next
            if temp.next.next is sc.head:
                break
        temp.next = sc.head
    def delete_pos(self, pos):
        temp = sc.head
        if temp is None:
            print("NoElementError : No element to delete")
            return
        for _ in range (pos-1):
            temp = temp.next

while True:
    val = int(input("Enter the val: "))
    if val == -1:
        break
    sc.add_begin(val)

m = main()
m.delete_beg()
sc.print_("After Deletion Begin")
m.delete_end()
sc.print_("After Deletion at end")