class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # return 0 in edge case
        if right == 0:
            return 0
        
        elif left == right:
            return left
        
        else:
            diff = right - left
            leftAndRight = left & right

            # this will AND the left and right to give us as many 0s as we can use for the base case
            init = list(str(bin(leftAndRight))[2:])

            index = len(init) - 1
            twoPower = 0
            while twoPower < len(init):
                if diff >= 2**twoPower:
                    init[index] = '0'
                twoPower += 1
                index -= 1
            return int(''.join(init), 2)



        
        

