class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        # intuition is to create a list of numbers that must be covered (example 1 needs 2, 3, 4, 5). Each interval
        # may cover some or all of the list of numbers. In example 1, there are 3 intervals necessary to cover the 
        # entire list. 
        #
        # Looked at some of the solutions just to see how to improve efficiency over the naive approach,
        # seems like sorting the list before trying to figure out the intervals is a good idea.
        # I wouldn't have thought of sorting, so I think using a dictionary might work here without
        # significant computational complexity?
        # 

        # create a dictionary for storing covered/not covered
        covered = {}

        # initialize the dictionary with False entries
        for i in range(left, right+1):
            covered[i] = False

        for i in covered:
            for start, end in ranges:
                if start<=i<=end:
                    covered[i] = True
                    break
            if covered[i] == False:
                return False

        return True

        # solution works, but is likey very slow
