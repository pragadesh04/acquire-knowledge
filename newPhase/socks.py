from collections import Counter
i = list(map(int,input().split()))

cal = Counter(i)
res = 0

for i,j in cal.items():
    if j % 2 != 0:
        res += 1
print(res)