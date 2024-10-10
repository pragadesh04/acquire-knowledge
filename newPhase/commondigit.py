from collections import Counter
o = input()
t = input()
th = input()

str = Counter(o + t + th)

for i,j in str.items():
    if(j == 3):
        print(i)