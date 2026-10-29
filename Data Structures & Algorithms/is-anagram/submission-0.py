class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = tuple(sorted(s))
        t = tuple(sorted(t))
        return s == t