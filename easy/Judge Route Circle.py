class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # for a in moves:
        f = False
        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
        	f = True
        return f
