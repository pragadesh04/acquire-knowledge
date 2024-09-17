"""
the input may contain charaters and long series of space but we need to just consider the words
"""

class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split(" ")
        return (len(list(x for x in s if x != '')))