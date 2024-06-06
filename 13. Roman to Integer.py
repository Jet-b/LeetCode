class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        neumerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        numbers = [neumerals[l] for l in s]
        total = 0
        for n in range(len(numbers)):
            
            if numbers[n] >= numbers[min(len(numbers)-1,n+1)]:
                total+=numbers[n]
            else:
                total-=numbers[n]
        return total


