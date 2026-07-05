class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        max_substr = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            max_substr = max(max_substr, r - l + 1)
            chars.add(s[r])
        return max_substr
