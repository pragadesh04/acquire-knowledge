n = int(input())
i = 1

while i<=n:
    i *= 2

i = ((n-(i//2))*2)+1
print(i)