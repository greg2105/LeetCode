class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # keep track of the smallest and second smallest, largest and second largest. 
        # Second value is the index (which array it comes from)
        minValue = (float('inf'), -1)
        prevMin = (float('inf'), -1)

        maxValue = (-float('inf'), -1)
        prevMax = (-float('inf'), -1)
        
        for i in range(len(arrays)):
            lastIndex = len(arrays[i]) - 1
            # The first index will always be the smallest in the array
            if arrays[i][0] < minValue[0]:
                prevMin = minValue
                minValue = (arrays[i][0], i)
            elif arrays[i][0] < prevMin[0]:
                prevMin = (arrays[i][0], i)

            # The last index will always be the largest in the array
            if arrays[i][lastIndex] > maxValue[0]:
                prevMax = maxValue
                maxValue = (arrays[i][lastIndex], i)
            elif arrays[i][lastIndex] > prevMax[0]:
                prevMax = (arrays[i][lastIndex], i)

        # if min and max are in same array, compare the max/prevMin with min/prevMax
        if minValue[1] == maxValue[1]:
            return max(maxValue[0] - prevMin[0], prevMax[0] - minValue[0])

        # Return the largest difference
        return maxValue[0] - minValue[0]