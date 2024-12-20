class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # obviously can't compute the factorial of every number here
        # can either use A. some math trick or B. dynamic programming or C. both. 
        # at n = 5, there is 1 trailing 0. At 10 there are 2, and at 15 there are 3. 
        # Just looking at factorials, it seems like every 5 we add a trailing 0.
        # so if our base case is 5 = 1 trailing 0, all we need to do is divide the number
        # by 5 and we will have the number of trailing 0s? Cant be this easy
        # 
        # So this implementation was correct for up to 33 factorial (I was taking the floor of the division)
        # 33 // 5 is 6, but the output should be 7. I see, so we should also divide by all exponentiations of 5.
        # So our largest number is 10^4. All exponentions of 5 are:
        # [5, 25, 125, 625, 3125]. 5^6 is 15,625. So basically we just check where our number lies on this list, 
        # and divide it by each integer that is to the left of where our number is, always using integer division

        # base case where there are no trailing 0s yet
        if n <= 4:
            return 0
        
        # use this to figure out how many of 5's exponentiations are in the number
        exponentiations = [5, 25, 125, 625, 3125]

        # trailing zeros counter
        trailingZeros = 0   

        # as an example, if we use 10, index will be 1. So we should only include values to the left of our index,
        # in this case we would only use 5
        for i in exponentiations:
            if n >= i:
                trailingZeros += n // i     

        return trailingZeros

        