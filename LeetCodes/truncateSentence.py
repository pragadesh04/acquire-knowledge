class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        val = []
        for i in range(k):
            val.append(s[i])
        return (' '.join(val))