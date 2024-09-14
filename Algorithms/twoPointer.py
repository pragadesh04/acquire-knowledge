"""
The Two pointer Algorithm to get the possiblities of the two numbers to get a target value
"""

arr = list(map(int, [x for x in range(1,10)]))
print(arr)

target = int(input("enter the target: "))

left = 0
right = len(arr)-1

while left < right:
    add = arr[left]+arr[right]
    if add == target:
        print(f"{arr[left]} + {arr[right]} = {target}")
        break
    elif add > target:
        right -=1
    elif add < target:
        left +=1
else:
    print("No Combinations")