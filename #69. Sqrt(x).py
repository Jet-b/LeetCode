
# base idea
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(0, x+1):
            if (i+1)**2 > x:
                return i
        