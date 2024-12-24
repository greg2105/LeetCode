# works but is very slow, beats 5%
class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        # A naive solution would be to keep some sort of dictionary that counts the number of times we have counted
        # a year. For example in [1950, 1961] we would add 1 to each year between 1950 and 1961. This would allow
        # us to return the key with the highest value. This is expensive though. 
        
        dictOfYears = {}
        
        # keep this to compare the populations
        maxPop = 0
        yearOfMax = 0

        # iterate through all the pairs
        for pair in logs:
            for years in range(pair[0], pair[1]):
                print(years)
                if years not in dictOfYears:
                    dictOfYears[years] = 1
                else:
                    dictOfYears[years] += 1
                
                # update maxPop
                if dictOfYears[years] > maxPop:
                    maxPop = dictOfYears[years]    
                    yearOfMax = years
                elif dictOfYears[years] == maxPop:
                    if years < yearOfMax:
                        yearOfMax = years
        
        return yearOfMax
                