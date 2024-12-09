class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # in this first part, we make a list of the largest subsets of consecutive integers. We will break these down later
        totalSum = 0
        
        # maintain two pointers to slice the array afterwards
        pointer1 = 0
        pointer2 = 1

        # shameless hardcoding of edgecases
        if len(nums) == 3:
            return 1
        elif len(nums) < 3:
            return 0

        # iterate through the entire array
        while pointer2 < len(nums):
            difference = abs(nums[pointer2] - nums[pointer2 - 1])
            
            # if adjacent numbers are not consecutive, and we do not have a streak yet
            elif difference != 1 and pointer2 - pointer1 == 1:
                pointer2 += 1
                pointer1 += 1

            # if adjacent numbers are not consecutive, but we did have a streak
            else:
                n = pointer2 - pointer1 - 1
                totalSum += ((n)*(n-1))/2
                pointer2 += 1
                pointer1 = pointer2 - 1
        
        # when the pointer2 goes out of bounds, add to sum one last time
        totalSum += ((pointer2 - pointer1 - 1)*(pointer2 - pointer1 - 1-1))/2

        return totalSum