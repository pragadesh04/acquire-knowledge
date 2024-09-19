"""
list is like ["++X","--X","X++"]
"""
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in range(len(operations)):
            print(i)
            if operations[i][0] == '+' or operations[i][-1] == '+':
                x +=1
            elif operations[i][0] == '-' or operations[i][-1] == '-':
                x-=1
        return x