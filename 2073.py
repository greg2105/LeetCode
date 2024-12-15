class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        # keep a running timer for num seconds
        time = 0 

        for i in range(len(tickets)):
            if i <= k:
                # any element before or at the kth index will iterate until either tickets[i] reaches 0, or until
                # tickets[k] reaches 0
                time += min(tickets[i], tickets[k])
            else:
                # any element after the kth index will only iterate tickets[k] - 1 times, because once we reach
                # tickets[k] = 0 we stop iterating.
                time += min(tickets[i], tickets[k] - 1)
        return time

        