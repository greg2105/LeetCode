class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dict to hold number of occurences
        charDict = {}

        # array to hold the multiplied characters
        charArray = []
        
        # count number of occurences
        for i in s:
            if i not in charDict:
                charDict[i] = 1
            else:
                charDict[i] += 1

        # multiply the character by number of occurences
        for i in sorted(charDict, key=charDict.get, reverse=True):
            charArray.append(i * charDict[i])
        
        return ''.join(charArray)