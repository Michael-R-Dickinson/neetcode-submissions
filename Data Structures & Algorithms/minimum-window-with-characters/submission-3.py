from collections import defaultdict
class Solution:
    def subsetFreqMap(self, m1, m2):
        # is m1 a subset of m2
        for k in m1:
            if m1[k] > m2.get(k, float('-inf')):
                return False
        return True

    def minWindow2(self, s: str, t: str) -> str:
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
        while True:
            while not self.subsetFreqMap(target_counts, counts):
                r += 1
                if r == len(s):
                    return min_substring
                if s[r] in target_chars:
                    counts[s[r]] +=1
                
            while s[l] not in target_chars:
                counts[s[l]] -= 1
                if counts[s[l]] <= 0:
                    del counts[s[l]]
                l += 1
            
            window_size = r - l + 1
            if window_size < min_substr_len:
                min_substring = s[l:r+1]
                min_substr_len = len(s[l:r+1])

            counts[s[l]] -= 1
            if counts[s[l]] <= 0:
                del counts[s[l]]
            l += 1
    def minWindow(self, s: str, t: str) -> str:
        """
        keep track of how many characters we have and how mayn we need
        use frequency map

        invariants (end of loop):
        - have 
        - counts - synced with r, l pointers


        start empty
        expand the string until valid
        contract the string until invalid - record each solution along the way

        """

        if t == "":
            return ""

        target_counts = defaultdict(int)
        for c in t:
            target_counts[c] += 1
        
        counts = defaultdict(int)
        l, r = 0, -1
        have = 0
        need = sum(target_counts.values())

        res_str = ""
        res_len = float('inf')

        while True:
            # expand
            while have != need:
                r += 1
                if r == len(s):
                    return res_str

                counts[s[r]] += 1
                # if we just added a character that we 'had' less of than we needed
                # increment have
                if counts[s[r]] <= target_counts[s[r]]:
                    have += 1
            
            while have == need:
                # this is a valid substring
                # record it as a potential solution
                window_size = r - l + 1
                if window_size < res_len:
                    window = s[l:r + 1]
                    res_str = window
                    res_len = window_size

                # shrink the window
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]

                # if we lost a necessary character, decrement have
                if counts[s[l]] < target_counts[s[l]]:
                    have -= 1
                l += 1




