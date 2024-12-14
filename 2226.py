class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        # so we are looking for the maximum number of candies each child can get, and 
        # each child can take at most one pile of candies. This makes the question far simpler.
        # From example two, we know that one edge case that we can check for before solving the question is looking
        # at if k > number of candies. We return 0 in this case.
        # the naive solution is to start with 1 candy per pile and check to see how many piles we get. Then increment the
        # candy per pile by 1, and see how many piles we get. We should stop once the number of piles is < k, and then return
        # candy per pile - 1. This would be very computationally intensive. We can try a binary search instead.
        
        # if we dont have enough candies to hand out
        if sum(candies) < k:
            return 0

        # binary search parameters
        
        # the lowest we can start with is 1
        low = 1

        # we can never increase the candy per pile to greater than the max value of the array
        high = max(candies)

        while low <= high:
            # reset mid each iteration
            mid = (high+low) // 2

            print(mid)
            numberOfPiles = sum(x // mid for x in candies) # integer division to find the floor of the result, cannot have
            # part of a candy

            if numberOfPiles >= k:
                low = mid + 1
            else:
                high = mid - 1

        return high


