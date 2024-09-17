"""
The code is about the FIZZBUZZ code
"""
# My Solution
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_arr = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                str_arr.append("FizzBuzz")
            elif i % 5 == 0:
                str_arr.append("Buzz")
            elif i % 3 == 0:
                str_arr.append("Fizz")
            else:
                str_arr.append(f"{i}")
        return str_arr

# Optimal Solution
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = [str(i) for i in range(1, n + 1)]
        for i in range(2, n, 3):
            l[i] = "Fizz"
        for i in range(4, n, 5):
            l[i] = "Buzz"
        for i in range(14, n, 15):
            l[i] = "FizzBuzz"
        return l