# beats 100%

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # keep a running sum
        totalSum = 0
        
        # maintain two pointers to slice the array afterwards
        pointer1 = 0
        pointer2 = 1

        # hardcoding of edgecase
        if len(nums) < 3:
            return 0

        # intialize difference to be the difference between the first two elements
        difference = nums[pointer2] - nums[pointer2 - 1]

        # iterate through the entire array
        while pointer2 < len(nums):
            prevDifference = difference
            difference = nums[pointer2] - nums[pointer2 - 1]
            
            # adjacent numbers have the same difference as the previous two
            if prevDifference == difference:
                pointer2 += 1

            # if adjacent numbers do not have the same difference, but we did have a streak
            else:
                # n = length of the subsequence
                n = pointer2 - pointer1
                
                if n > 3:
                    totalSum += ((n-2)*(n-1))//2
                # the formula doesn't work for a sequence of exactly 3
                elif n == 3:
                    totalSum += 1
                difference = nums[pointer2] - nums[pointer2 - 1] if pointer2 < len(nums) else 0
                pointer2 += 1
                pointer1 = pointer2 - 2
        
        # when the pointer2 goes out of bounds, add to sum one last time (if we had a streak)
        n = pointer2 - pointer1
        if n > 3:
            print("yes")
            totalSum += ((n-2)*(n-1))//2
        elif n == 3:
            totalSum += 1

        return totalSum