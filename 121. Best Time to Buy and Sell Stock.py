# solution takes too long

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxVal = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                val = prices[j] - prices[i]
                if val > maxVal:
                    maxVal = val
        return maxVal