# currently beats 6.12%. Only 16ms runtime
class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        # so we are given the coordinates of the lower left and upper right hand corners of two rectangles. 
        # if we want to return the area, really all we need to do is determine the x and y overlap and multiply those
        # dimensions together. 
        #
        # I found an equation that should work for the overlap between the two rectangles
        # max(ax1, bx1) - min(ax2, bx2) works for the x values
        # max(ay1, by1) - min(ay2, by2) works for the y values
        # this will give us a range (assuming we use the absolute value of the range)
        
        # calculate the individual rectangle areas
        rectangle1Area = abs(ax1 - ax2) * abs(ay1 - ay2)
        rectangle2Area = abs(bx1 - bx2) * abs(by1 - by2)

        # intialize overlap to 0
        overlap = 0
        xOverlap = 0
        yOverlap = 0

        # see if the two rectangles overlap. In order the cases are
        # first left side overlaps
        # first right side overlaps
        # second left side overlaps
        # second right side overlaps
        if (ax1 >= bx1 and ax1 <= bx2) or (ax2 >= bx1 and ax2 <= bx2) or (bx1 >= ax1 and bx1 <= ax2) or (bx2 >= ax1 and bx2 <= ax2):
            # calculate the x overlap from the two rectangles
            xOverlap = abs(max(ax1, bx1) - min(ax2, bx2))
        if (ay1 >= by1 and ay1 <= by2) or (ay2 >= by1 and ay2 <= by2) or (by1 >= ay1 and by1 <= ay2) or (by2 >= ay1 and by2 <= ay2):
            # calculate the y overlap from the two rectangles
            yOverlap = abs(max(ay1, by1) - min(ay2, by2))
        
        print(xOverlap)
        print(yOverlap)


        # subtract the overlap
        total = rectangle1Area + rectangle2Area - (xOverlap * yOverlap)
        
        return total

