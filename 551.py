class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        numAs = 0
        numLs = 0
        aCriteria = False
        lCriteria = True
        for record in s:
            if record == 'A':
                numAs += 1
                numLs = 0
            elif record == 'P':
                numLs = 0
            else:
                numLs += 1
            if numLs >= 3:
                lCriteria = False
        if numAs < 2:
            aCriteria = True
        return lCriteria and aCriteria