
# base idea, does not work for large numbers, but works for small numbers
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(0, x+1):
            if (i+1)**2 > x:
                return i

# binary search solution, much better

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid
        return right
