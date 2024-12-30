class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        total = 0
        for command in commands:
            if command == "RIGHT":
                total += 1
            elif command == "LEFT":
                total -= 1
            elif command == "UP":
                total -= n
            else:
                total += n
        return total