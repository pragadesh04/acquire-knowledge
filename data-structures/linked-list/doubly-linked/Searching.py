import utils
dll = utils.double()
class searching:
    def search(self, key):
        i = 0
        j = 0
        temp = dll.head
        while temp:
            if temp.data == key:
                print(f"The element from forward {key} found at index : {i}")
                break
            else:
                i+=1
                temp = temp.next
        while temp.next:
            temp = temp.next
        while temp:
            if temp.data == key:
                return f"The element from backward {key} found at index : {-j -1}"
            j+=1
            temp = temp.prev
          
sch = searching()
inp = utils.input_()
val = 0
while True:
    val = inp.inp()
    if val == -1:
        break
    dll.add(val)    
dll.print_()
print()
data = int(input("Enter the data for position enter 0: "))
print (sch.search(data))