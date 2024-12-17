class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # very easy, can just loop through all subsequences of 3 characters and see if there are duplicates. Maybe
        # convert to a set and see if its the same?
        def helperFunction(word):
            for x in set(word):
                if word.count(x) > 1:
                    return False
            return True
        
        pointer1 = 0
        pointer2 = 3
        validSubstrings = 0
        while pointer2 <= len(s):
            word = s[pointer1:pointer2]
            if helperFunction(word) == True:
                validSubstrings += 1
            pointer1 += 1
            pointer2 += 1
        return validSubstrings