class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        # okay the initial intuition is to loop through the bank array. If sum of the string is > 0,
        # then we know we have security devices. We can store the sum in a variable like firstRow
        # then we iterate through the array again with firstRow initialized to some number. Once we encounter
        # A row that has a sum > 0, then we just need to calculate the number of lasers (fully connected network)
        # if each device is connected to the other devices, I think its just numLasers in first row * numLasers in second
        # row. Then we can initialize firstRow to the new number of devices that was in secondRow, and repeat the process.
        # if we never reach a 'second row' we never calculate the product and we just end the loop.

        # keep a running total of number of lasers
        total = 0

        # keep a variable for numLasers in 'firstRow'
        firstRow = 0

        # another one for the 'secondRow'
        secondRow = 0

        for row in bank:
            summation = row.count('1')
            if summation >= 1:
                total += summation * firstRow
                firstRow = summation
        

        # return what we've added up total. Returns 0 if nothing happens in the for loop
        return total
        