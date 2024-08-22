import sclutils

sc = sclutils.scll()

class main:
    def minmax(self):
        min = max = sc.head.data
        temp = sc.head
        while True:
            if temp.data > max:
                max = temp.data
            if temp.data < min:
                min = temp.data
            temp = temp.next
            if temp == sc.head:
                break

        print(f"The maximum is: {max}\nThe Minimum is: {min}")

m = main()
val = 0
while True:
    val = int(input("Enter the value: "))
    if val == -1:
        break
    sc.add_begin(val)

sc.print_()
print()
m.minmax()