from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        sliding window
        keep track of:
            - frequency map of chars in window: keep track of how many replacements we need
            - most frequent character: for knowing which char we don't have to replace
        
        walk the list, at each step:
        - update freq map and most frequent char
        - if we have enough replacements remaining, bump r
        - if not, bump l
        """
        
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res            



        