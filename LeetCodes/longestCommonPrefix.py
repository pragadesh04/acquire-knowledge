"""
Longest Common Prefix: best Optimal Answer from another user
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        first = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(first) != 0:
                first = first[0:len(first)-1]
                print(first)
                if first == "":
                    return ""
        return first