'''
we iterate by letter until we've reached the length of the longest one

if the previous letters were equal:
    - then the empty one must be first
    - can early return if we find a single non-equal letter
'''


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True
        
        lex_order = {letter: idx for idx, letter in enumerate(order)}

        for first_word_idx in range(len(words) - 1):
            first = words[first_word_idx]
            second = words[first_word_idx + 1]

            # verify they're in order
            for i in range(max(len(first), len(second))):
                '''
                walk letters until we reach one of these cases:
                    - out of letters in one word -> if we're out of letters from the first, its in order
                    - first[i] != second[i] -> if first[i] is before second[i] lexographically, then its in order
                '''
                

                # if we're out of letters from one:
                if i == min(len(first), len(second)):
                    if i == len(first):
                        print(i)
                        break
                    return False

                if first[i] != second[i]:
                    # check lexographically
                    if lex_order[first[i]] < lex_order[second[i]]:
                        print(first[i], second[i])
                        break
                    return False
        return True
