# val = input()

# v = 0

# v = 1 if val[0] == 'u' else 0
# print(v)

# for i in range(1,len(val)):
#     if val[i-1] != val[i]:
#         if val[i] == 'u':
#             v += 1
#         elif val[i] == 'd':
#             v -= 1

# print(v)

v =0
val = input()
for i in val:
    if i == 'v':
        v += 1
    elif i == 'd':
        v-=1
print(v)