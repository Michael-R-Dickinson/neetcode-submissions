from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        for char in s:
            s_count[char] += 1
        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1
        return s_count == t_count
        