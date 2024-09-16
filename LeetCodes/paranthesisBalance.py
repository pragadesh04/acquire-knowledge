"""
Its not correct just checks the blance for the number of the brackets
"""
class Solution:
    def isValid(self, s: str) -> bool:
        flag = True
        arr = []
        stack = {')':'(', '}':'{',']':'['}

        for i in s:
            if i in stack:
                top = arr.pop() if arr else '#'
                if stack[i] != top:
                    return False
            else:
                arr.append(i)
        return not arr