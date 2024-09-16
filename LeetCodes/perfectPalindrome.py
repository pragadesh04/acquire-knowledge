# My code:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                temp += i.lower()
        l = 0
        r = len(temp)-1

        while l<r:
            if temp[l] != temp[r]:
                return False
            l+=1
            r-=1
        else:
            return True

# Optimal code:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True
        