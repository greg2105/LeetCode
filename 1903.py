class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # naive solution is easy, just wonder if theres a faster way to do this.
        # can split the string into individual digits, this way we can check even/odd
        # we definitely want to start from the largest digit and work our way down
        # could sort it? I think sorting is O(n) so this would be slower than just iterating
        # through the list once. Can check for max(num), which might also be an O(n) operation since
        # its checking every value. I think just iterating through the list might actually be the fastest.
        # didnt realize we arent just checking digits, but also subtrings. I guess we should start with the full length of
        # the substring, and then reduce the window size by 1 each time, because this will lead to finding the largest
        # number first.
        # 
        # so I implemented a solution, but the runtime was too long. I think doing % 2 takes a while with really large numbers,
        # and it's unnecessary since we just need the last digit to be 1, 3, 5, 7, or 9.
        # I don't see how I can find the largest odd number any faster, we are returning as soon as we find it. 
        # we also start with the largest window possible. The instance I failed on I don't think had a single
        # odd ending in it... I guess we can use a base case to get around that
        # 
        # well it works, but is only faster than 9.33% of solutions.
        #
        oddEndings = ['1', '3', '5', '7', '9']
        total = 0

        for i in (num.count(x) for x in oddEndings):
            total += i
        if total == 0:
            return ""
        
        # base case is when the entire string is the largest odd number
        largestPossible = int(num)
        if largestPossible % 2 != 0:
            return str(largestPossible)
        
        # if base case doesn't return an odd number, set the intial window size which we will decrement with each
        # loop
        windowSize = len(num) - 1

        # set max number to 0 for the condition of the while loop
        maxNumber = 0

        while windowSize > 0:
            # use offset to slice the string
            offset = 0
            while offset + windowSize <= len(num):
                # get the last digit and see if its in oddEndings
                if num[offset:offset+windowSize][-1] in oddEndings and int(num[offset:offset+windowSize]) > maxNumber:
                    maxNumber = num[offset:offset+windowSize]
                offset += 1
            # return after the first loop that initializes maxNumber to something else
            if maxNumber > 0:
                return maxNumber
            windowSize -= 1

        # return an empty string if we don't find any larger values than 0
        return ""