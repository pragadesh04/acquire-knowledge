"""
Code to find the string is Isomorphic or not
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        flag = True
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] not in mapping.values():
                    mapping[s[i]] = t[i]
                else:
                    return False
            else:
                if mapping[s[i]] != t[i]:
                    flag = False
        return flag