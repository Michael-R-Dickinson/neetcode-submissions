from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l = 0
        r = len(s1) - 1 # inclusive

        # have a sliding window the size of s1
        # slide it across all of s2 and check for permutations of s1 at each step
        # m = len(s1), n = len(s2)
        # O(m * n)

        s1_chars = defaultdict(int)
        for char in s1:
            s1_chars[char] += 1

        window = s2[l:r + 1]
        chars = defaultdict(int)
        for char in window:
            chars[char] += 1
        if chars == s1_chars:
            return True

        l += 1
        r += 1
        while r < len(s2):
            just_left = s2[l - 1] # just left the window
            just_entered = s2[r] # new character

            chars[just_left] -= 1
            chars[just_entered] += 1

            if chars[just_left] == 0:
                del chars[just_left]

            if chars == s1_chars:
                return True

            l += 1
            r += 1
        
        return False

