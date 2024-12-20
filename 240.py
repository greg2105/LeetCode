# beats 94%. 

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # intuition is some sort of dual binary search: once for the column value and once for the row value.
        #
        # We aren't necessarily looking for an exact number, we want to either find the number itself if its the first
        # entry of the row, or we want to find the row right above a value that is greater than the value we are looking
        # for. And in the row search, we are looking for exact number. It may not exist, so we should consider that case.
        #
        # Our binary search finds the maximum row that our target could be located in. From there,
        # we have to figure out whether our target is in that row or not. There could be many rows (from 0 to mid) that
        # our target could be in.
        # 
        # If we iterate through the rows and we hit a number larger than our target, we can stop. 


        # low value for searching the columns
        columnLow = 0

        # high value for searching the columns
        columnHigh = len(matrix) - 1

        while columnLow <= columnHigh:
            mid = (columnLow + columnHigh) // 2

            # if we happen to find the value as the first entry of a row
            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] > target:
                if mid >= 1 and matrix[mid-1][0] < target:
                    mid = mid-1
                    break
                columnHigh = mid-1
            
            elif matrix[mid][0] < target:
                if mid != len(matrix) - 1 and matrix[mid+1][0] > target:
                    break
                columnLow = mid+1 

        # iterate through the rows of matrix up till the maximum value
        for row in matrix[0:mid+1]:
            rowLow = 0
            rowHigh = len(row) - 1
            
            while rowLow <= rowHigh:
                mid = (rowLow + rowHigh) // 2

                if row[mid] == target:
                    return True
                
                elif row[mid] > target:
                    rowHigh = mid-1

                else:
                    rowLow = mid+1
        return False
