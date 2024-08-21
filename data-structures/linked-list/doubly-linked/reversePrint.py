import utils as add

dll = add.double()

class reverse:
    def printRev(self):
        temp = dll.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

rev = reverse()
inp = add.input_()
val = 0
while True:
    val = inp.inp()
    if val == -1:
        break
    dll.add(val)
    
dll.print_()
rev.printRev()