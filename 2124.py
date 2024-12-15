class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # return false if first character is a b, otherwise loop through
        if s[0] != 'a' and 'a' in s:
            return False
        else:
            encounteredB = False
            for i in s:
                if i == 'b':
                    encounteredB = True
                if i == 'a' and encounteredB:
                    return False

        return True
