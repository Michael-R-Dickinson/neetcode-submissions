from collections import defaultdict

'''
needed_freqs map keeps track of how many of each character we need at the current step

we also keep a num_needed list
-> keeps track of how many elements we still need

when we add an element to the window we check - is it in chars_needed
If it is:
- subtract from needed_freqs[char]
- AND we need to see whether we can subtract from num_needed - basically how close we are to having all char counts needed

Note: we always subtract from needed_freqs[char] and it can go negative because negative simply signifies we have more than enough of a character - keep track so in case later we lose some of that char from the window, we still know that we have excess

when to subtract from num_needed: when we gain a character that we didn't already have enough of
- check if num_needed > 0 -> if so num_needed -= 1

when we remove an element from the window:
If in chars_needed:
- add to needed_freqs[char] += 1
same logic for num_needed as with adding: if chars_needed AFTER adding > 0 -> increase num_needed

If num_needed == 0:
record substring length

expand the window until num_needed == 0, then contract until > 0
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # the set of all characters that we need some of:
        # - gives a quick lookup for whether we need to make a change to 
        #   needed_freqs
        chars_needed = set(t)
        num_needed = len(t)
        needed_freqs =  defaultdict(int)
        for char in t:
            needed_freqs[char] += 1
        
        best_len = float('inf')
        best = ""

        # both r and l are inclusive
        l = 0
        for r in range(len(s)):
            r_char = s[r]
            if r_char not in chars_needed:
                continue
            
            # Add new character to window
            if needed_freqs[r_char] > 0:
                num_needed -= 1
            needed_freqs[r_char] -= 1

            # while we still have a valid substring - shrink window
            # do we want to shrink until the window is invalid? 
            while num_needed == 0:
                # record valid substring len
                substr_len = r - l + 1
                if substr_len < best_len:
                    best_len = substr_len
                    best = s[l:r+1]

                # shrink
                l_char = s[l]
                if l_char in chars_needed:
                    needed_freqs[l_char] += 1
                    if needed_freqs[l_char] > 0:
                        num_needed += 1
                l += 1
        return best if best_len != float('inf') else ""
            




        
        
