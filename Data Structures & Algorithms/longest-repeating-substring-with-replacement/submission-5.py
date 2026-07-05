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
        
        freq_map = defaultdict(int)
        max_freq = 0
        max_window_size = 0

        l = 0
        for r in range(len(s)):
            freq_map[s[r]] += 1
            if freq_map[s[r]] > max_freq:
                max_freq = freq_map[s[r]]

            while (r - l + 1) - max_freq > k:
                l += 1
                freq_map[s[l - 1]] -= 1

            max_window_size = max(r - l + 1, max_window_size)           

        return max_window_size
            



        