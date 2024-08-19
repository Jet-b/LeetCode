
# bad solution, could use backwardz iteration along digits to avoid converting to string
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for i in digits:
            num += str(i)
        num = int(num) +1
        return [int(i) for i in str(num)]