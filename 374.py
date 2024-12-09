# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n, new = 0):
        """
        :type n: int
        :rtype: int
        """
        # set bounds for recursion
        low, high = 1, n

        # loop through recursive calls
        while low <= high:
            mid = (low+high)//2
            hint = guess(mid)

            if hint == 0:
                return mid
            elif hint == -1:
                high = mid - 1
            else:
                low = mid + 1
        