class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # sort the list so we can find the overlapping intervals
        points = sorted(points)
        
        # assume we need at least one dart for the starting balloon
        totalArrows = 1

        # keep a variable that will serve as a comparison later
        end = points[0][1]

        for item in points[1:]:
            # if the start of the current balloon is greater than the end of the previous balloon, we need a new arrow
            if item[0] > end:
                totalArrows += 1
                end = item[1]
            else:
                end = min(item[1], end)

        return totalArrows