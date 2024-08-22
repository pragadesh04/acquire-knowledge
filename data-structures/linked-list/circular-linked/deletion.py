import sclutils as scl
sc = scl.scll()

class main:
    def delete_beg(self):
        sc.head = sc.head.next
        sc.last.next = sc.head
        
