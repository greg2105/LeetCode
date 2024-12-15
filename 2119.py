class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # intuition is a number can only ever *not* be reversed if its trailing digits are 0 and the number is greater 
        # than 0
        if num > 0 and str(num)[-1] == '0': # convert the number to a string to get the last digit
            return False
        return True