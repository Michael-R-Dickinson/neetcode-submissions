from collections import defaultdict
class Solution:
    def subsetFreqMap(self, m1, m2):
        # is m1 a subset of m2
        for k in m1:
            if m1[k] > m2.get(k, float('-inf')):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        """
        sliding window
        freq hashmap

        [A X Y A A A A  Z O U Z O D | Y X  A Z | V]

        init shortest substring = ""

        expand window until valid:
        - right pointer moves - if it reaches the end of the list
            we know there are no more valid substrings
        contract until minimal:
        - until contracting any more would violate valididty

        record the substring
        increment the left poitner by one, continue
        """
        if len(t) == 0:
            return ""

        target_chars = set([c for c in t])
        target_counts = defaultdict(int)
        for c in t:
            target_counts[c] += 1

        min_substring = ""
        min_substr_len = float('inf')
        counts = defaultdict(int)
        l, r = 0, -1
        print('target', dict(target_counts))
        while True:
            while not self.subsetFreqMap(target_counts, counts):
                r += 1
                if r == len(s):
                    return min_substring
                if s[r] in target_chars:
                    counts[s[r]] +=1
                    
                print(s[r], dict(counts))
                
            print('starting contraction', l, r, s[l])
            while s[l] not in target_chars:
                print(l, s[l])
                counts[s[l]] -= 1
                if counts[s[l]] <= 0:
                    del counts[s[l]]
                l += 1
            
            window_size = r - l + 1
            print('found str', s[l:r+1])
            if window_size < min_substr_len:
                print('found MINIMUM', s[l:r+1])
                min_substring = s[l:r+1]
                min_substr_len = len(s[l:r+1])

            counts[s[l]] -= 1
            if counts[s[l]] <= 0:
                del counts[s[l]]
            l += 1

                


