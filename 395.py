



# Got far into this one, then couldn't figure out the recursion. Wrote notes on a solution found elsewhere. Putting it here for learning




class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # count the occurences of each character in the string
        charCounts = collections.Counter(s)

        # maintain a pointer to identify the start of a substring
        pointer1 = 0

        # initialize the maximum length we've discovered so far
        maxLength = 0

        # enumerate lists the items and their respective indices
        # for example, a string of 'this' would result in
        # [(0, 't'), (1, 'h'), (2, 'i'), (3, 's')]
        for index, character in enumerate(s):
            if charCounts[character] < k:
                # recursively call the function with the substring before hitting the delimiting character
                maxLength = max(maxLength, self.longestSubstring(s[pointer1:index], k))
                
                # move the start index of the next substring
                pointer1 = index + 1

        # if we never hit a delimiting character, just return the length of the string
        return len(s) if pointer1 == 0 else max(maxLength, self.longestSubstring(s[pointer1:], k))