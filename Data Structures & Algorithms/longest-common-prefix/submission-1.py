class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_len = 0
        # if 0 characters match prefix_len = 0 -> produces ''
        shortest_string_len = min(len(s) for s in strs)
        for i in range(shortest_string_len):
            all_strings_at_i_equal = len(set(s[i] for s in strs))==1
            if not all_strings_at_i_equal:
                break
            prefix_len += 1
        return strs[0][0:prefix_len]

