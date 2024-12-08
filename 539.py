class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # 1440 is the same way of saying 0
        zeroEquivalent = 1440
        timePointsInMinutes = []
        addedZeroEquivalent = False
        
        # convert all entries to total minutes
        for time in timePoints:
            hours, minutes = map(int, time.split(':'))
            total_minutes = hours * 60 + minutes
            timePointsInMinutes.append(total_minutes)

            # only add the zero equivalent if we have a zero. The boolean prevents duplicates.
            if total_minutes == 0 and addedZeroEquivalent == False:
                timePointsInMinutes.append(zeroEquivalent)
                addedZeroEquivalent = True
        
        # set minDifference to arbitrarily large value
        minDifference = float('inf')

        # sort in increasing order
        timePointsInMinutes.sort()

        # find difference between adjactent pairs, update minDifference accordingly
        for i in range(len(timePointsInMinutes)-1):
            difference = timePointsInMinutes[i+1] - timePointsInMinutes[i]
            minDifference = min(minDifference, difference)

        # for the last entry, compute distance between it and the first entry. Only do this if we don't have a 0 in there.
        if timePointsInMinutes[0] != 0:
            upperDifference = 1440 - timePointsInMinutes[-1]
            lowerDifference = timePointsInMinutes[0]
            difference = upperDifference + lowerDifference
            minDifference = min(minDifference, difference)

        # return the min difference
        return minDifference