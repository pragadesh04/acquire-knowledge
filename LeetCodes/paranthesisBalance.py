"""
Its not correct just checks the blance for the number of the brackets
"""
class Solution:
    def isValid(self, s: str) -> bool:
        flag = True
        arr = []
        for i in s:
            arr.append(i)
        arr = sorted(arr)
        
        for i in range(0,len(arr)-1):
            val = 2
            if arr[i] == '(':
                val = 1
            if arr[i] and ord(arr[i]) == ord(arr[i+1])-val:
                arr[i] = None
                arr[i+1] = None
            print(i)
        
        return True if arr.count(None) == len(s) else False