import utils as add
dll = add.double()
class minmax:
    def minMax(self):
        temp = dll.head
        print(temp.data)
        min = dll.head.data
        max = dll.head.data
        if temp.data is None:
            print("no element")
            return {"max":None, "min":None}

        while temp.next:
            if temp.data < min:
                min = temp.data
            if temp.data > max:
                max = temp.data
            temp = temp.next
        return {"max":max, "min":min}

mm = minmax()
inp = add.input_()
val = 0

while True:
    val = inp.inp()
    if val == -1:
        break
    dll.add(val)
    
dll.print_()
print(mm.minMax())