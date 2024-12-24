class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        # naive is to make 8 arrays and hardcode the colors lol.
        # the other way to do it is to split the rows between even and odds. If the number is even, the color
        # scheme matches one pattern, if its odd the pattern flips.
        # we can just make one array and then use that to invert the result if we are on an even row
        oddRows = {'a': False, 'b': True, 'c': False, 'd': True, 'e': False, 'f': True, 'g': False, 'h': True}

        if int(coordinates[1]) % 2 != 0:
            return oddRows[coordinates[0]]
        else:
            return not oddRows[coordinates[0]]