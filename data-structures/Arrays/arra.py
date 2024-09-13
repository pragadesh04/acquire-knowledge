from array import array

arr = array('i',[])
print(arr)

arr.insert(-1,90)
arr.insert(-1,70)
arr.insert(-1,80)
arr.insert(-1,100)
arr.insert(-1,1)
print(arr)

arr.pop(0)
print(arr.pop())