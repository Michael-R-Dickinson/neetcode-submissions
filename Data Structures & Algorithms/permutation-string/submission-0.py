from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l = 0
        r = len(s1) - 1 # inclusive

        # have a sliding window the size of s1
        # slide it across all of s2 and check for permutations of s1 at each step

        s1_chars = defaultdict(int)
        for char in s1:
            s1_chars[char] += 1

        while r < len(s2):
            window = s2[l:r + 1]

            chars = defaultdict(int)
            for char in window:
                chars[char] += 1
            
            if chars == s1_chars:
                return True

            l += 1
            r += 1
        
        return False

