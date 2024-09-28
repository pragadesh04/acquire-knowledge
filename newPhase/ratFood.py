rat,unit,n= int(input()),int(input()),int(input())

house = list(map(int,input().split()))
base = 0
res = 0
tot = rat * unit

for i in range(n):
    if base < tot:
        res += 1
        base += house[i]

print(i, res)
if res-1 == i:
    print(res)
else:
    print("0")