# note: doesn't have the best runtime (beats 23%)

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # Need some criteria for sequences that work and sequences that dont.
        # For example, for stones = [0,1,3,5,6,8,12,17], a failed sequence would be reaching
        # 3, and then choosing k=3 to travel to 6. In this case, no value of k-1, k, or k+1 can bring us to an 
        # additional stone. So we did not reach stones[-1]. 

        # convert stones to a set for faster lookup if there are duplicates
        stone_set = set(stones)

        # keep track of which stones we've already visited
        visited = set()

        def tryAllPossible(value, jump):
            print(value, jump)
            # if we landed on the last stone in the list
            if value == stones[-1]:
                return True

            # if we already tried this value and jump combo, it returned false, so return False. Or if not a next stone.
            if (value, jump) in visited or value not in stone_set or jump <= 0:
                return False

            # add the current node to the visited list
            visited.add((value, jump))

            # try k - 1, k, k + 1
            for tryJump in (jump - 1, jump, jump + 1):
                if tryAllPossible(value + tryJump, tryJump):
                    return True
            
            return False

        # start from the second index of stones. Jump = 1 because this is guaranteed.
        return tryAllPossible(1, 1)