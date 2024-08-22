import sclutils
sc = sclutils.scll()

class main:
    def search(self, key):
        temp = sc.head
        i=0
        while True:
            if temp.data == key:
                print (f"The element found at : {i}")
                return
            temp  = temp.next
            i+=1
            if temp == sc.head:
                break
        else:
            print("NoElementError : NO element to Perform an operations")
            return
        print(f"NoElementFound : Searched and cannot find {key} in List")

m = main()
val = 0
while True:
    try:
        val = int(input("Enter the value : "))
    except:
        val = 0
        
    if val == -1:
        break
    sc.add_begin(val)

sc.print_("List are: \n")
print()
key = int(input("Enter element to search: "))
m.search(key)