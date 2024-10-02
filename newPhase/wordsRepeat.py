string = input().split()
flag = True
for i in string:
    if string.count(i) > 1:
        flag = False
print(flag)