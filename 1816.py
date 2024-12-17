class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Intuition is to split the string by spaces, cut the list using slicing,
        # then combine the string using spaces
        s = s.split(' ')
        s = s[0:k]
        s = (' ').join(s)
        return s