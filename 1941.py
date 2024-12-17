class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert s to a set for faster iteration
        setS = set(s)

        # count the first character that appears in s. We will end up counting this character twice, but this is negligible
        firstCount = s.count(s[0])

        # loop through the set, count each character as they appear in the original string
        for character in setS:
            count = s.count(character)
            # if the count does not match the count of the first character in s, return False
            if count != firstCount:
                return False

        return True