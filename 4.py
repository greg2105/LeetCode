class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # we know the length of the two arrays, with len(nums1) and len(nums2)
        # we also know that the median is going to be the middle number, so if the length is even the median
        # will be the average of the two middle numbers
        # Additionally, the arrays are sorted, so we can get around merging these two arrays.

        # these lengths will be used to find the median index
        lengthOfNums1 = len(nums1)
        lengthOfNums2 = len(nums2)
        lengthOfMergedArray = lengthOfNums1 + lengthOfNums2

        # hardcode edge cases
        if lengthOfMergedArray <= 1:
            if nums1:
                return nums1[0]
            else:
                return nums2[0]
        
        # keep two pointers so that we can compare values
        nums1pointer = 0
        nums2pointer = 0
        
        # for odd case
        median = 0

        # for even case
        medians = ()

        # in the case that the length of the merged array is odd
        if lengthOfMergedArray % 2 != 0:
            # use integer division to round down. len 3 will give index 1, len 5 will give index 2, etc.
            median = lengthOfMergedArray // 2
            print(median)

            mergedArrayIndex = nums1pointer + nums2pointer  

            lastIncrement1 = False
            lastIncrement2 = False
            while mergedArrayIndex < median:
                if nums1[nums1pointer] < nums2[nums2pointer] and nums1pointer < len(nums1)-1:
                    nums1pointer += 1
                    lastIncrement1 = True
                    lastIncrement2 = False
                else:
                    nums2pointer += 1
                    lastIncrement2 = True
                    lastIncrement1 = False

                # keep track of the mergedArray index 
                mergedArrayIndex = nums1pointer + nums2pointer
            if lengthOfNums1 == 1 or lengthOfNums2 == 1:
                return min(nums1[nums1pointer], nums2[nums2pointer])
            return nums1[nums1pointer] if lastIncrement1 else nums2[nums2pointer]

        # in the case that the length of the merged array is even
        else:
            median = lengthOfMergedArray / 2
            print(median)
            
            # these two will be added and then averaged
            firstNumber = nums1[0]
            secondNumber = nums2[0]

            mergedArrayIndex = nums1pointer + nums2pointer  

            while mergedArrayIndex < median:
                if nums1[nums1pointer] < nums2[nums2pointer] and nums1pointer < len(nums1)-1:
                    nums1pointer += 1
                    if nums1pointer + nums2pointer == median:
                        secondNumber = nums1[nums1pointer]
                    if nums1pointer + nums2pointer == median - 1:
                        firstNumber = nums1[nums1pointer]
                        print("yes", firstNumber)
                else:
                    nums2pointer += 1 
                    if nums1pointer + nums2pointer == median-1:
                        secondNumber = nums2[nums2pointer]
                    if nums1pointer + nums2pointer == median - 2:
                        firstNumber = nums2[nums2pointer]
                
                # keep track of the mergedArray index 
                mergedArrayIndex = nums1pointer + nums2pointer
                

            print("nums1pointer", nums1pointer)
            print("nums2pointer", nums2pointer)
            print(firstNumber)
            print(secondNumber)
            return (float(firstNumber) + float(secondNumber)) / 2.0
        



        