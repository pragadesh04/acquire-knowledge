"""
Adding till the target is >= given target in a minimal subArray
"""

values = [2,3,1,2,4,3]
l = r = 0
minimum = 1000000000
target = (int(input("Enter the target: ")))
temp = 0
while r<len(values):
    temp += values[r]
    while temp>=target:
        minimum = r-l+1
        temp -= values[l]
        l+=1
    r+=1
print(minimum)