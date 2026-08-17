# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binSearch(bot, top):
            if top < bot:
                # number cannot be found
                return -1

            mid = (top + bot) // 2

            result = guess(mid)
            if result == 0:
                return mid
            if result == 1:
                return binSearch(mid+1, top)
            else:
                return binSearch(bot, mid-1)

        return binSearch(1, n)
            