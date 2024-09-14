"""
The Two pointer Algorithm to get the possiblities of the two numbers to get a target value
"""

arr = list(map(int, [x for x in range(1,10)]))
print(arr)

target = int(input("enter the target: "))

left = 0
right = len(arr)-1
i = 0

while i<len(arr):
    add = arr[left]+arr[right]
    if add == target:
        print(f"{arr[left]} + {arr[right]} = {target}")
        left +=1    
    elif add > target:
        right -=1
    elif add < target:
        left +=1
    i+=1