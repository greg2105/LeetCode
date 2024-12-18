class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # should be very easy. Just start from the min number and decrement until a divisor works. Though, if the larger number
        # is odd, we can skip iterations by decrementing by 2 if the smaller number is also odd. 
        largest = max(nums)
        smallest = min(nums)
        if largest % smallest == 0:
            return smallest
        else:
            # define a subtractor to use to decrement the smallest number
            subtractor = 0
            # if both numbers are even or if both numbers are odd
            if (largest % 2 != 0 and smallest % 2 != 0) or (largest % 2 == 0 and smallest % 2 == 0):
                while (smallest % (smallest - subtractor) != 0 or largest % (smallest - subtractor) != 0):
                    # decrement by 2 if they are both even or both odd
                    subtractor += 2
            else:
                while (smallest % (smallest - subtractor) != 0 or largest % (smallest - subtractor) != 0):
                    subtractor += 1
        return (smallest - subtractor)