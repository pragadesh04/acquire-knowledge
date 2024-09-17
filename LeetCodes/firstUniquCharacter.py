"""
Findeing the first unique character in a string got result from the user
"""

import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        val = Counter(s)

        for i,j in val.items():
            if j == 1:
                return s.index(i)
        return -1