from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t: return True
        return Counter(s) == Counter(t)