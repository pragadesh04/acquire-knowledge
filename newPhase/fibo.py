i = int(input())
a = []
a.append(0)
a.append(1)


for i in range(2,i+2):
    a.append(a[i-1]+a[i-2])
    print(a,i)
print(a)