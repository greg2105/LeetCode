# faster than 48.99%. The approach was the most optimal, the only difference was that I created a new array
# and used that to modify nums, instead of just modifying nums itself.
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # intuition is that the array will at some point revert to its original state, this is where k = len(nums). So we
        # only need to consider displacements after this point
        if k > len(nums):
            k = k % len(nums)
            print(k)
            newNums = nums[(len(nums) - k):len(nums)]
            newNums += nums[0:(len(nums)-k)]
            for i in range(len(newNums)):
                nums[i] = newNums[i]
        else:
            newNums = nums[(len(nums) - k):len(nums)]
            newNums += nums[0:(len(nums)-k)]
            for i in range(len(newNums)):
                nums[i] = newNums[i]


