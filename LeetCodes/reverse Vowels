class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a','e','i','o','u']
        new = []
        for i in s:
            if i.lower() in vow:
                new.append(i)
        s = list(s)
        j = len(new)-1
        for i in range(len(s)):
            if s[i].lower() in vow:
                s[i] = new[j]
                j-=1
        print(s)
        return ''.join(s)