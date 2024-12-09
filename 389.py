class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # the only letter added is the letter in t
        if len(s) == 0:
            return t
        
        for i in t:
            if i not in s:
                return i
            else:
                if t.count(i) != s.count(i):
                    return i